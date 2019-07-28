import unittest
from unittest.mock import patch
from inventory_management import main


class MainTest(unittest.TestCase):
    """ This class handles test cases for the main test file """

    @patch('builtins.input', lambda *args: '1')
    def test_main_menu_goes_to_add_new_item(self):
        self.assertEqual(main.main_menu(), main.main_menu('1'))

    @patch('builtins.input', lambda *args: '2')
    def test_main_menu_goes_to_get_item_info(self):
        self.assertEqual(main.main_menu(), main.main_menu('2'))

    @patch('builtins.input', lambda *args: 'q')
    def test_main_menu_goes_to_quit(self):
        self.assertEqual(main.main_menu(), main.main_menu('q'))

    def test_get_price_of_item(self):
        self.assertEqual(main.get_price(), 50)

    def test_get_info_of_non_existent_item(self):
        with patch('builtins.input', return_value='0'):
            main.item_info()

    def test_get_info_of_item(self):
        with patch('builtins.input', side_effect=['1', 'fake', '100', 'N', 'N']):
            main.add_new_item()
        with patch('builtins.input', return_value='1'):
            main.item_info()

    @staticmethod
    def test_add_new_generic_item():
        with patch('builtins.input', side_effect=['2', 'fake', '100', 'N', 'N']):
            main.add_new_item()

    @staticmethod
    def test_add_new_furniture_item():
        with patch('builtins.input', side_effect=['3', 'fake', '100', 'Y', 'Wool', 'L']):
            main.add_new_item()

    @staticmethod
    def test_add_new_electric_appliance_item():
        with patch('builtins.input', side_effect=['4', 'fake', '100', 'Y', 'GE', '120V']):
            main.add_new_item()
