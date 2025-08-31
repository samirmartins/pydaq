from PySide6.QtWidgets import QFileDialog, QWidget
from pydaq.uis.ui_PyDAQ_Benchmarking import Ui_Form
from PySide6.QtWidgets import QApplication
import time
import serial
import warnings
import nidaqmx

ard_vpb = 1  # Conversion factor, if needed

class BenchmarkingWidget(QWidget, Ui_Form):
    def __init__(self, com="COM5", *args):
        super(BenchmarkingWidget, self).__init__()
        self.setupUi(self)
        self.close_button.released.connect(self.close_window)
        self.start_button.released.connect(self.inicialize_benchmarking)
        self.com_port = com
        self.ser = None 

    def close_window(self):
        self.close()

    def inicialize_benchmarking(self, periods_s=[2, 1, 0.5, 0.2, 0.1, 0.01, 0.001, 0.0001, 0.00001], base_duration=5, allowed_delay_percent=2.0):
        print("Testing Arduino Serial sampling performance...\n")
        self.value_beench.appendPlainText("Testing SERIAL sampling performance...\n")
        QApplication.processEvents()

        try:
            self.ser = serial.Serial(self.com_port, 115200, timeout=0.05)
            print(f"✅ Serial Port {self.com_port} open with success.")
        except serial.SerialException as e:
            warnings.warn(f"⚠️ It was not possible to open the Serial Port {self.com_port}: {e}")
            print("❌ Aborting benchmarking.")
            return  

        min_period_recommended = None
        best_stable_period = None

        for Ts in periods_s:
            duration_s = max(base_duration, 5 * Ts)  # garante pelo menos 5 amostras
            sample_times = []
            delays = 0
            start = time.perf_counter()
            next_sample_time = start

            while time.perf_counter() - start < duration_s:
                now = time.perf_counter()
                if now >= next_sample_time:
                    t0 = now
                    try:
                        line = self.ser.readline().decode("utf-8").strip()
                        if line.isdigit():
                            value = int(line) * ard_vpb
                        else:
                            continue
                    except Exception as e:
                        print("Serial read error:", e)
                        continue

                    t1 = time.perf_counter()
                    sample_times.append(t1)

                    next_sample_time += Ts

                    if t1 - t0 > Ts:
                        delays += 1
                else:
                    time.sleep(max(0, next_sample_time - now))

            total_samples = len(sample_times)
            if total_samples < 2:
                print(f"Period: {Ts:.3f} s | No valid readings ❌\n")
                self.value_beench.appendPlainText(f"Period: {Ts:.3f} s | No valid readings ❌\n")
                QApplication.processEvents()
                continue

            intervals = [t2 - t1 for t1, t2 in zip(sample_times[:-1], sample_times[1:])]
            jitter = max(intervals) - min(intervals)
            avg_cycle = sum(intervals) / len(intervals)
            theoretical_samples = duration_s / Ts
            delay_percent = (delays / total_samples) * 100
            status = "✅ OK" if delay_percent <= allowed_delay_percent else "⚠️ FAIL"

            print(f"Sample Period: {Ts:.3f} s | Samples: {total_samples:5} | "
                  f"Theoretical: {theoretical_samples:6.1f} | Delays: {delays:4} "
                  f"({delay_percent:5.1f}%) | Avg cycle: {avg_cycle:7.3f} s | "
                  f"Jitter: {jitter:7.3f} s | {status}")
            self.value_beench.appendPlainText(
                f"Target Ts {Ts:.3f} s  | Avg Ts: {avg_cycle:.3f} s | {status}"
            )
            QApplication.processEvents()

            if delay_percent <= allowed_delay_percent:
                best_stable_period = Ts
                min_period_recommended = avg_cycle * 1.2

        if self.ser:
            try:
                if self.ser.is_open:
                    self.ser.close()
                    print(f"🔌 Serial Port {self.com_port} closed.")
            except Exception:
                pass

        if min_period_recommended:
            print("\n✅ Ideal sampling period (with 20% safety margin): "
                  f"{min_period_recommended:.3f} s")
            print(f"➡️  You can safely use Ts = {best_stable_period:.3f} s or greater.")
            self.value_beench.appendPlainText(f"➡️  You can safely use Ts = {best_stable_period:.3f} s or greater.")
            QApplication.processEvents()
        else:
            print("\n❌ No stable sampling period was found. Try higher values or check serial performance.")


class BenchmarkingNIWidget(QWidget, Ui_Form):
    def __init__(self, nidaq_channel="Dev1/ai0", *args):
        super().__init__(*args)
        self.setupUi(self)
        self.close_button.released.connect(self.close_window)
        self.start_button.released.connect(self.inicialize_benchmarking)
        self.nidaq_channel = nidaq_channel
        self.task = None

    def close_window(self):
        self.close()

    def inicialize_benchmarking(self, periods_s=None, base_duration=5):
        if periods_s is None:
            periods_s = [10, 5, 2, 1, 0.5, 0.2, 0.1]
        print("Testing NI-DAQ sampling performance...\n")
        self.value_beench.appendPlainText("Testing NI-DAQ sampling performance...\n")
        QApplication.processEvents()

        try:
            self.task = nidaqmx.Task()
            self.task.ai_channels.add_ai_voltage_chan(self.nidaq_channel)
        except Exception as e:
            print(f"❌ Could not initialize NI-DAQ task: {e}")
            return

        min_period_recommended = None
        best_stable_period = None

        for Ts in periods_s:
            duration_s = max(base_duration, 5 * Ts)
            delays = 0
            cycle_times = []
            start = time.perf_counter()

            while (time.perf_counter() - start) < duration_s:
                t0 = time.perf_counter()

                try:
                    value = self.task.read()
                except Exception as e:
                    print("NI-DAQ read error:", e)
                    continue

                t1 = time.perf_counter()
                cycle_time = t1 - t0
                cycle_times.append(cycle_time)

                if cycle_time > Ts:
                    delays += 1
                else:
                    time.sleep(max(0, Ts - cycle_time))

            total_samples = len(cycle_times)
            if total_samples == 0:
                print(f"Period: {Ts:.3f} s | No valid readings ❌\n")
                self.value_beench.appendPlainText(f"Period: {Ts:.3f} s | No valid readings ❌\n")
                QApplication.processEvents()
                continue

            avg_cycle = sum(cycle_times) / total_samples
            delay_percent = (delays / total_samples) * 100
            status = "✅ OK" if delays == 0 else "⚠️ FAIL"

            print(f"Sample Period: {Ts:.3f} s | Samples: {total_samples:5} | Delays: {delays:4} "
                  f"({delay_percent:5.1f}%) | Avg cycle: {avg_cycle:7.4f} s | {status}")
            self.value_beench.appendPlainText(f"Sample Period: {Ts:.3f} s | {status}\n")
            QApplication.processEvents()

            if delays == 0:
                best_stable_period = Ts
                min_period_recommended = avg_cycle * 1.2

        if self.task:
            self.task.close()
            print(f"🔌 NI-DAQ task closed.")

        if min_period_recommended:
            print("\n✅ Ideal sampling period (with 20% safety margin): "
                  f"{min_period_recommended:.3f} s")
            print(f"➡️  You can safely use Ts = {best_stable_period:.3f} s or greater.")
            self.value_beench.appendPlainText(f"{min_period_recommended:.3f} s")
        else:
            print("\n❌ No stable sampling period was found. Try higher values or check device performance.")
