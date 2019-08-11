"""
Unit Tests for all modules and classes from the inventory_management dir
"""

import InventoryClass
import FurnitureClass
from ElectricAppliancesClass import *
import main
import market_prices

from unittest import TestCase
from unittest.mock import patch


class ElectricAppliancesTest(TestCase):
    def test_return_dict(self):
        appliance = ElectricAppliances('a', 'b', 'c', 'd', 'e', 'f')
        td = {}
        td['productCode'] = 'a'
        td['description'] = 'b'
        td['marketPrice'] = 'c'
        td['rentalPrice'] = 'd'
        td['brand'] = 'e'
        td['voltage'] = 'f'
        self.assertDictEqual(appliance.return_as_dictionary(), td)


class MainMenuTest(TestCase):
    def test_get_latest_price(self):
        with patch('builtins.input', side_effect="2"):
            self.assertEqual(main.main_menu(), main.item_info)

