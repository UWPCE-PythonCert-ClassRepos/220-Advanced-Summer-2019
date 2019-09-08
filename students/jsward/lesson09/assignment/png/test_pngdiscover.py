"""
grade l9 part 3
"""
import pytest
import pngdiscover

working_dir = "/Users/james/code/220-Advanced-Summer-2019/students/jsward/lesson09/assignment/png/data"

@pytest.fixture
def _test_list_png_files():
    """ structure from test """
    return {
        f"{working_dir}/furniture/chair": ["metal_chair_back_isometric_400_clr_17527.png"],
        f"{working_dir}/furniture/chair/couch": ["sofa_400_clr_10056.png"],
        f"{working_dir}/furniture/table": ["table_with_cloth_400_clr_10664.png", "basic_desk_main_400_clr_17523.png", "desk_isometric_back_400_clr_17524.png"],
        f"{working_dir}/new": ["chairs_balancing_stacked_400_clr_11525.png", "hotel_room_400_clr_12721.png"],
        f"{working_dir}/old": ["sitting_in_chair_relaxing_400_clr_6028.png", "couple_on_swing_bench_400_clr_12844.png"]}


def test_list_png_files(_test_list_png_files):
    """ student generates """
    pngdiscover.find_files(working_dir)
    assert pngdiscover.data == _test_list_png_files
