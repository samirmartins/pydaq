from PySide6.QtWidgets import QFileDialog, QWidget, QMessageBox
from pydaq.uis.ui_PyDAQ_Benchmarking import Ui_Form
from pydaq.guis.error_window_gui import Error_window
import time
import serial

ser = None  # Inicialmente vazio
ard_vpb = 1  # Conversion factor, if needed

class BenchmarkingWidget(QWidget, Ui_Form):
    def __init__(self, com="COM5", *args):
        super(BenchmarkingWidget, self).__init__()
        self.setupUi(self)
        self.close_button.released.connect(self.close_window)
        self.start_button.released.connect(self.inicialize_benchmarking)
        self.com_port = com  # Default COM port

        # Tenta abrir a porta serial aqui
        global ser
        try:
            ser = serial.Serial(self.com_port, 115200, timeout=0.05)
        except serial.SerialException as e:
            QMessageBox.critical(self, "Serial Error", f"Could not open port {self.com_port}:\n{e}")
            ser = None

    def close_window(self):
        self.close()

    def inicialize_benchmarking(self, periods_ms=[10, 5, 2, 1, 0.5, 0.2, 0.1, 0.01, 0.001, 0.0001], duration_s=5):
        if ser is None or not ser.is_open:
            QMessageBox.warning(self, "Serial Not Available", "Serial port is not open or available.")
            return

        print(f"Testing SERIAL sampling performance for {duration_s} seconds per period...\n")
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
                    line = ser.readline().decode("utf-8").strip()
                    if line.isdigit():
                        value = int(line) * ard_vpb
                    else:
                        continue
                except Exception as e:
                    print("Serial read error:", e)
                    continue

                t1 = time.perf_counter()
                cycle_time = t1 - t0
                cycle_times.append(cycle_time)

                if cycle_time > period_s:
                    delays += 1
                else:
                    time.sleep(period_s - cycle_time)

            total_samples = len(cycle_times)

            if total_samples == 0:
                print(f"Period: {period_ms:7.5f} ms | No valid readings ❌\n")
                continue

            avg_cycle = sum(cycle_times) / total_samples
            delay_percent = (delays / total_samples) * 100
            status = "✅ OK" if delays == 0 else "⚠️ FAIL"

            print(f"Period: {period_ms:7.5f} ms | Samples: {total_samples:5} | Delays: {delays:4} "
                f"({delay_percent:5.1f}%) | Avg cycle: {avg_cycle*1000:7.4f} ms | {status}")

            if delays == 0:
                best_stable_period = period_ms
                min_period_recommended = avg_cycle * 1.2

        if min_period_recommended:
            print("\n✅ Ideal sampling period (with 20% safety margin): "
                f"{min_period_recommended*1000:.3f} ms")
            print(f"➡️  You can safely use Ts = {best_stable_period} ms or greater.")
        else:
            print("\n❌ No stable sampling period was found. Try higher values or check serial performance.")
