"""Integration test"""
import sys
sys.path.insert(0, './inventory_management')

import unittest
import inventory_class
import furniture_class
import electric_appliances_class
import market_prices
import main
from unittest.mock import patch, call

class FullTest(unittest.TestCase):
    """Test Menu"""
    def test_main_menu(self):
        with patch('builtins.input', side_effect=["error_input", "1"]):
            self.assertEqual(main.main_menu(), main.add_new_item)
        with patch("builtins.input", side_effect="2"):
            self.assertEqual(main.main_menu(), main.item_info)
        with patch("builtins.input", side_effect=["end_program", "q"]):
            self.assertEqual(main.main_menu(), main.exit_program)

    """Test Adding"""
    @staticmethod
    def test_add_new_furniture_item():
        with patch('builtins.input', side_effect=['1', 'furn', '100', "y", 'wood', 'small']):
            main.add_new_item()
    @staticmethod
    def test_add_new_electric_appliance_item():
        with patch('builtins.input', side_effect=['2', 'elec', '200', "n", "y", 'GE', '21 GW']):
            main.add_new_item()
    @staticmethod
    def test_add_new_inventory_item():
        with patch('builtins.input', side_effect=['3', 'inven', '300', "n", "n"]):
            main.add_new_item()

    @staticmethod
    def test_check_inventory():
            furniture_expected = {'product_code': '1', 'description': 'furn', 'market_price': 24, 'rental_price': '100', 'material': 'wood', 'size': 'small'}
            assert(main.FULL_INVENTORY['1']==furniture_expected)
            electric_expected = {'product_code': '2', 'description': 'elec', 'market_price': 24, 'rental_price': '200', 'brand': 'GE', 'voltage': "21 GW"}
            assert(main.FULL_INVENTORY['2']==electric_expected)
            inventory_expected = {'product_code': '3', 'description': 'inven', 'market_price': 24, 'rental_price': '300'}
            assert(main.FULL_INVENTORY['3']==inventory_expected)
