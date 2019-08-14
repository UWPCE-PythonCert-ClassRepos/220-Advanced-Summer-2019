"""
check good works the same, and is faster
"""
import sys
sys.path.insert(0,'../src')
import poor_perf as p
import good_perf as g


def test_assess_preformance():
    """ compare """
    poor = p.analyze('..//data//exercise.csv', 'Street')
    good = g.analyze('..//data//exercise.csv', 'Street')
    poor_elapsed = poor[1] - poor[0]
    good_elapsed = good[1] - good[0]
    assert good_elapsed < poor_elapsed
    assert poor[2] == good[2]
    assert poor[3] == good[3]
