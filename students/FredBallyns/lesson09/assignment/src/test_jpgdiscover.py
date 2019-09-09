"""
grade l9 part 3
"""
import pytest
from pprint import pprint

import jpgdiscover as sut

@pytest.fixture
def _test_find_files():
    """ structure from test """
    return  [
        "../data/furniture/chair", ["metal_chair_back_isometric_400_clr_17527.png"],
        "../data/furniture/chair/couch", ["sofa_400_clr_10056.png"],
        "../data/furniture/table", ["basic_desk_main_400_clr_17523.png", "desk_isometric_back_400_clr_17524.png", "table_with_cloth_400_clr_10664.png"],
        "../data/new", ["chairs_balancing_stacked_400_clr_11525.png", "hotel_room_400_clr_12721.png"],
        "../data/old", ["couple_on_swing_bench_400_clr_12844.png", "sitting_in_chair_relaxing_400_clr_6028.png"]]

def test_find_files(_test_find_files):
    """ student geneartes """
    jpgs = sut.find_files("../data",".png")
    pprint(_test_find_files)
    print("")
    pprint(jpgs)
    assert jpgs == _test_find_files
