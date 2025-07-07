import time

def testar_periodos_automatico(periodos_ms=[10, 5, 2, 1, 0.5, 0.2, 0.1, 0.01, 0.001, 0.0001, 0.00001], duracao_s=10):
   
    
    print(f"Testando desempenho de amostragem por {duracao_s}s para cada período...\n")

    for periodo_ms in periodos_ms:
        periodo_s = periodo_ms / 1000
        atrasos = 0
        tempos = []
        inicio = time.perf_counter()

        while (time.perf_counter() - inicio) < duracao_s:
            t0 = time.perf_counter()

            
            t1 = time.perf_counter()
            tempo_execucao = t1 - t0
            tempos.append(tempo_execucao)

            if tempo_execucao > periodo_s:
                atrasos += 1
            else:
                time.sleep(periodo_s - tempo_execucao)

        total_amostras = len(tempos)
        media_execucao = sum(tempos) / total_amostras
        percentual_atraso = (atrasos / total_amostras) * 100

        status = "✅ OK" if atrasos == 0 else "⚠️  Falhou"
        print(f"Período: {periodo_ms} ms | Amostras: {total_amostras:4} | Atrasos: {atrasos:4} "
              f"({percentual_atraso:.1f}%) | Média ciclo: {media_execucao*1000:.3f} ms | {status}")

# Exemplo de uso:
testar_periodos_automatico()
