import serial
import time
import matplotlib.pyplot as plt

# Configura a porta serial do Arduino
ser = serial.Serial("COM5", 115200, timeout=1)

timestamps = []
values = []

print("📡 Coletando dados do Arduino... pressione Ctrl+C para parar.")
try:
    while True:
        line = ser.readline().decode("utf-8").strip()
        if not line:
            continue

        try:
            t_str, v_str = line.split(",")
            t = int(t_str) / 1e6   # converte microssegundos -> segundos
            v = int(v_str)
            timestamps.append(t)
            values.append(v)
        except ValueError:
            continue  # ignora linhas inválidas

except KeyboardInterrupt:
    print("\n⏹️ Coleta interrompida pelo usuário.")

finally:
    ser.close()
    print("🔌 Serial fechado.")

# --- Processamento ---
if len(timestamps) > 2:
    # Calcula intervalos entre amostras
    intervals = [t2 - t1 for t1, t2 in zip(timestamps[:-1], timestamps[1:])]
    avg_Ts = sum(intervals) / len(intervals)
    jitter = max(intervals) - min(intervals)
    fs = 1 / avg_Ts

    print(f"\n✅ Resultados da aquisição no hardware:")
    print(f"  Amostras: {len(values)}")
    print(f"  Ts médio: {avg_Ts*1000:.3f} ms")
    print(f"  Frequência média: {fs:.1f} Hz")
    print(f"  Jitter: {jitter*1000:.3f} ms")

    # --- Plot ---
    plt.figure()
    plt.plot(timestamps, values, label="Sinal bruto")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Valor ADC")
    plt.title("Aquisição no Arduino (com timestamp do hardware)")
    plt.grid(True)
    plt.legend()
    plt.show()
