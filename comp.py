import cProfile
import pstats
from pydaq.pydaq_global import PydaqGui


profiler = cProfile.Profile()
profiler.enable()

PydaqGui()

profiler.disable()
profiler.dump_stats("saida.prof")

stats = pstats.Stats(profiler)
stats.strip_dirs().sort_stats('cumtime').print_stats(30)

