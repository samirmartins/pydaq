from PySide6.QtWidgets import QFileDialog, QWidget
from pydaq.uis.ui_PyDAQ_Benchmarking import Ui_Form
from PySide6.QtWidgets import QApplication
import time
import serial
import warnings
import nidaqmx
import matplotlib.pyplot as plt

ard_vpb = 1  

def find_arduino():
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "CH340" in port.description:
                return port.device
        return None

class BenchmarkingWidget(QWidget, Ui_Form):
    def __init__(self, com=None, *args):
        super(BenchmarkingWidget, self).__init__()
        self.setupUi(self)
        self.close_button.released.connect(self.close_window)
        self.start_button.released.connect(self.inicialize_benchmarking)

        if com is None:
            com = find_arduino()
        

        self.com_port = com
        self.ser = None 

    def close_window(self):
        self.close()

    def inicialize_benchmarking(self, period_s=[1, 0.5, 0.2, 0.1, 0.01, 0.001, 0.0001], duration_s=5, allowed_delay_percent=2.0):
        print(f"Testing Arduino Serial sampling performance for {duration_s} seconds per period...\n")
        self.value_beench.appendPlainText(f"Testing SERIAL sampling performance for {duration_s} seconds per period...\n")
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
        results = []  

        for Ts in period_s:
            period_s = Ts
            sample_times = []
            delays = 0
            start = time.perf_counter()
            next_sample_time = start + Ts  
            sample_count = 0

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
                    sample_count += 1

                    next_sample_time = start + (sample_count + 1)*Ts

                    if t1 - t0 > period_s:
                        delays += 1
                else:
                    time.sleep(max(0, next_sample_time - now))

            total_samples = len(sample_times)
            if total_samples < 2:
                print(f"Period: {period_s:7.5f} s | No valid readings ❌\n")
                self.value_beench.appendPlainText(f"Period: {period_s:7.5f} s | No valid readings ❌\n")
                QApplication.processEvents()
                continue

            
            intervals = [t2 - t1 for t1, t2 in zip(sample_times[:-1], sample_times[1:])]
            if len(intervals) > 1:
                intervals = intervals[1:]

            jitter = max(intervals) - min(intervals)
            avg_cycle = sum(intervals) / len(intervals)
            theoretical_samples = duration_s / period_s
            delay_percent = (delays / total_samples) * 100
            status = "✅ OK" if delay_percent <= allowed_delay_percent else "⚠️ FAIL"

            print(f"Sample Period: {period_s:7.5f} s | Samples: {total_samples:5} | "
                f"Theoretical: {theoretical_samples:6.1f} | Delays: {delays:4} "
                f"({delay_percent:5.1f}%) | Avg cycle: {avg_cycle:7.5f} s | "
                f"Jitter: {jitter:7.3f} s | {status}")
            self.value_beench.appendPlainText(
                f"Target Ts {period_s:7.5f} s  | Avg Ts: {avg_cycle:7.5f} s | {status}"
            )
            QApplication.processEvents()

            results.append((period_s, avg_cycle, jitter, status))

            if delay_percent <= allowed_delay_percent:
                best_stable_period = period_s
                min_period_recommended = avg_cycle * 1.2

        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"🔌 Serial Port {self.com_port} closed.")

        if min_period_recommended:
            print("\n✅ Ideal sampling period (with 20% safety margin): "
                f"{min_period_recommended:.3f} s")
            print(f"➡️  You can safely use Ts = {best_stable_period} s or greater.")
            self.value_beench.appendPlainText(f"➡️  You can safely use Ts = {best_stable_period} s or greater.")
            QApplication.processEvents()
        else:
            print("\n❌ No stable sampling period was found. Try higher values or check serial performance.")

        
        if results:
            Ts_values = [r[0] for r in results]
            avg_values = [r[1] for r in results]
            jitter_values = [r[2] for r in results]

            plt.errorbar(Ts_values, avg_values, yerr=jitter_values, fmt='o-', capsize=5, label="Avg Ts ± Jitter")
            plt.plot(Ts_values, Ts_values, 'r--', label="Target Ts")
            plt.xscale("log")
            plt.yscale("log")
            plt.xlabel("Target Ts (s)")
            plt.ylabel("Measured Avg Ts (s)")
            plt.title("Benchmarking Ts vs Measured Avg Ts")
            plt.legend()
            plt.grid(True, which="both", ls="--", lw=0.5)
            plt.show()


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

    def inicialize_benchmarking(self, periods_ms=None, duration_s=5):
        if periods_ms is None:
            periods_ms = [10, 5, 2, 1, 0.5, 0.2, 0.1, 0.01]
        print(f"Testing NI-DAQ sampling performance for {duration_s} seconds per period...\n")
        self.value_beench.appendPlainText(f"Testing NI-DAQ sampling performance for {duration_s} seconds per period...\n")
        QApplication.processEvents()

        try:
            self.task = nidaqmx.Task()
            self.task.ai_channels.add_ai_voltage_chan(self.nidaq_channel)
        except Exception as e:
            print(f"❌ Could not initialize NI-DAQ task: {e}")
            return

        min_period_recommended = None
        best_stable_period = None

        for period_ms in periods_ms:
            period_s = period_ms / 1000
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

                if cycle_time > period_s:
                    delays += 1
                else:
                    time.sleep(max(0, period_s - cycle_time))

            total_samples = len(cycle_times)
            if total_samples == 0:
                print(f"Period: {period_ms:7.5f} ms | No valid readings ❌\n")
                self.value_beench.appendPlainText(f"Period: {period_ms:7.5f} ms | No valid readings ❌\n")
                QApplication.processEvents()
                continue

            avg_cycle = sum(cycle_times) / total_samples
            delay_percent = (delays / total_samples) * 100
            status = "✅ OK" if delays == 0 else "⚠️ FAIL"

            print(f"Sample Period: {period_ms:7.5f} s | Samples: {total_samples:5} | Delays: {delays:4} "
                  f"({delay_percent:5.1f}%) | Avg cycle: {avg_cycle*1000:7.4f} ms | {status}")
            self.value_beench.appendPlainText(f"Sample Period: {period_ms:7.5f} s | {status}\n")
            QApplication.processEvents()

            if delays == 0:
                best_stable_period = period_ms
                min_period_recommended = avg_cycle * 1.2

        if self.task:
            self.task.close()
            print(f"🔌 NI-DAQ task closed.")

        if min_period_recommended:
            print("\n✅ Ideal sampling period (with 20% safety margin): "
                  f"{min_period_recommended*1000:.3f} ms")
            print(f"➡️  You can safely use Ts = {best_stable_period} ms or greater.")
            self.value_beench.appendPlainText(f"{min_period_recommended*1000:.3f} ms")
        else:
            print("\n❌ No stable sampling period was found. Try higher values or check device performance.")
