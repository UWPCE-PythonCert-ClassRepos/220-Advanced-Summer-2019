import unittest
from unittest.mock import patch
from inventory_management.main import main_menu

class MainTest(unittest.TestCase):
    """ This class handles test cases for the main test file """

    def test_main_menu(self):
        with patch('builtins.input', side_effect=2):
            main_menu()