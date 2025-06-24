import cProfile
import pstats
from pydaq.pydaq_global import PydaqGui

# Cria e inicia o profiler
profiler = cProfile.Profile()
profiler.enable()

# Executa sua GUI
PydaqGui()

# Finaliza e salva os dados de profiling
profiler.disable()
profiler.dump_stats("saida.prof")

# (opcional) Imprime no console os mais custosos
stats = pstats.Stats(profiler)
stats.strip_dirs().sort_stats('cumtime').print_stats(30)

