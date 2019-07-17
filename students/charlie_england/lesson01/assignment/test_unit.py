import sys
import unittest
sys.path.insert(0,'./inventory_management')
from main import main_menu, add_new_item, item_info
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import MagicMock
import electric_appliances_class
import furniture_class
import inventory_class
from market_prices import get_latest_price

class ElectricAppliancesTest(TestCase):

    def test_return_as_dict(self):
        lamp = electric_appliances_class.ElectricAppliances(1234, 'lamp', 25.00, 7.00, 'ikea', '25 watts')
        lamp_test_dict = {
            'description':'lamp',
            'marketPrice':25.00,
            'rentalPrice':7.00,
            'productCode':1234,
            'brand':'ikea',
            'voltage':"25 watts",
            }
        for k, v in lamp.return_as_dictionary().items():
            self.assertEqual(v, lamp_test_dict[k], f'Comparing {k} = {v}, supposed to be {k} = {lamp_test_dict[k]}')

class FurnitureClassTest(TestCase):

    def test_return_as_dict(self):
        couch = furniture_class.Furniture(5669, 'couch', 350.00, 25.00, 'synthetic', 'L')
        couch_test_dict = {
            'description':'couch',
            'marketPrice':350.00,
            'rentalPrice':25.00,
            'productCode':5669,
            'material':"synthetic",
            'size':'L'
            }
        for k, v in couch.return_as_dictionary().items():
            self.assertEqual(v, couch_test_dict[k], f'Comparing {k} = {v}, supposed to be {k} = {couch_test_dict[k]}')

class InventoryClassTest(TestCase):

    def test_return_as_dict(self):
        inven_item = inventory_class.Inventory(123,'random_item',8.00,1.00)
        inven_dict_test = {
            'productCode': 123,
            'description': 'random_item',
            'marketPrice': 8,
            'rentalPrice': 1,
            }
        for k, v in inven_item.return_as_dictionary().items():
            self.assertEqual(v, inven_dict_test[k], f'Comparing {k} = {v}, supposed to be {k} = {inven_dict_test[k]}')

class MainTest(TestCase):

    def test_main_menu(self):
        with patch("builtins.input", side_effect="2"):
            self.assertEqual(main_menu(), item_info)
        with patch('builtins.input', side_effect='1'):
            self.assertEqual(main_menu(), add_new_item)

    def test_add_new_item(self):
        with patch("builtins.input", side_effect=[123, 'couch', 7, 'y', 'synthetic', 'L']):
            mock_couch = furniture_class.Furniture()
            test_couch = add_new_item()
            self.assertEqual(test_couch.return_as_dictionary,'working')

    # @patch('main.item_info', return_value=123)
    # def test_item_info_123(self,input):
    #     self.assertEqual(item_info(),"Item not found in inventory")

class MarketPriceTest(TestCase):

    def test_market_price(self):
        val = 24
        self.assertEqual(val,get_latest_price(val),f'{val} is equal to {get_latest_price(val)}')

    
if __name__ == "__main__":
    unittest.main()