import pstats

p = pstats.Stats('out.profile')

p.strip_dirs().sort_stats("cumulative", "name").print_stats(0.5)