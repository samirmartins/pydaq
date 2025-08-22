import time
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import warnings

def benchmark_nidaq(device="Dev1", channel="ai0", terminal_config="RSE",
                    periods_ms=[10, 5, 2, 1, 0.5, 0.2, 0.1], duration_s=5):
    """
    Realiza um benchmarking da performance de aquisição usando uma placa NI-DAQ.
    
    Parameters:
        device (str): Nome do dispositivo NI (ex: "Dev1").
        channel (str): Canal analógico de entrada (ex: "ai0").
        terminal_config (str): Configuração do terminal ("RSE", "Diff", "NRSE").
        periods_ms (list): Lista de períodos de amostragem a testar, em milissegundos.
        duration_s (float): Duração de cada teste, em segundos.
    """

    print(f"Testing NI-DAQ sampling performance for {duration_s} seconds per period...\n")

    term_map = {
        "RSE": TerminalConfiguration.RSE,
        "Diff": TerminalConfiguration.DIFFERENTIAL,
        "NRSE": TerminalConfiguration.NRSE
    }

    min_period_recommended = None
    best_stable_period = None

    for period_ms in periods_ms:
        period_s = period_ms / 1000
        delays = 0
        cycle_times = []
        start = time.perf_counter()

        try:
            task = nidaqmx.Task()
            task.ai_channels.add_ai_voltage_chan(
                f"{device}/{channel}",
                terminal_config=term_map[terminal_config]
            )
        except nidaqmx.errors.DaqError as e:
            warnings.warn(f"❌ Failed to open NI-DAQ channel: {e}")
            return

        while (time.perf_counter() - start) < duration_s:
            t0 = time.perf_counter()

            try:
                value = task.read()
            except nidaqmx.errors.DaqError as e:
                warnings.warn(f"NI-DAQ read error: {e}")
                continue

            t1 = time.perf_counter()
            cycle_time = t1 - t0
            cycle_times.append(cycle_time)

            if cycle_time > period_s:
                delays += 1
            else:
                time.sleep(period_s - cycle_time)

        task.close()

        total_samples = len(cycle_times)
        if total_samples == 0:
            print(f"Period: {period_ms:7.5f} ms | No valid readings ❌\n")
            continue

        avg_cycle = sum(cycle_times) / total_samples
        delay_percent = (delays / total_samples) * 100
        status = "✅ OK" if delays == 0 else "⚠️ FAIL"

        print(f"Sample Period: {period_ms:7.5f} s | Samples: {total_samples:5} | Delays: {delays:4} "
              f"({delay_percent:5.1f}%) | Avg cycle: {avg_cycle*1000:7.4f} ms | {status}")

        if delays == 0:
            best_stable_period = period_ms
            min_period_recommended = avg_cycle * 1.2  # 20% margem de segurança

    if min_period_recommended:
        print("\n✅ Ideal sampling period (with 20% safety margin): "
              f"{min_period_recommended*1000:.3f} ms")
        print(f"➡️  You can safely use Ts = {best_stable_period} ms or greater.")
    else:
        print("\n❌ No stable sampling period was found. Try higher values or check DAQ performance.")
