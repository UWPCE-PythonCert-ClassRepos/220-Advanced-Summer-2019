import sys
from unittest import TestCase
from unittest.mock import patch

sys.path.insert(0, './inventory_management')

from inventory_management.furniture_class import Furniture
from inventory_management.market_prices import get_latest_price
from inventory_management.inventory_class import Inventory
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management import main

class ElectricApplianceClassTest(TestCase):
    def test_electric_appliance(self):
        lamp_test_dict = {
                'description': 'lamp',
                'market_price': 25.00,
                'rental_price': 7.00,
                'product_code': 1234,
                'brand': 'ikea',
                'voltage': "25 watts",
            }
        lamp = ElectricAppliances(**lamp_test_dict)
        for key, val in lamp.return_as_dictionary().items():
            self.assertEqual(val, lamp_test_dict[key], 
                             f'Comparing {key} = {val}, ' +
                             'supposed to be {key} = {lamp_test_dict[key]}')

class FurnitureClassTest(TestCase):
    def test_furniture(self):
        couch_test_dict = {
                'description': 'couch',
                'market_price': 350.00,
                'rental_price': 25.00,
                'product_code': 5669,
                'material': 'synthetic',
                'size': 'L'
            }
        couch = Furniture(**couch_test_dict)
        for key, val in couch.return_as_dictionary().items():
            self.assertEqual(val, couch_test_dict[key], 
                             f'Comparing {key} = {val}, ' +
                             'supposed to be {key} = {couch_test_dict[key]}')

class InventoryClassTest(TestCase):
    def test_inventory(self):
        inventory_dict_test = {
                'product_code': 123,
                'description': 'random_item',
                'market_price': 8,
                'rental_price': 1,
            }
        inventory_item = Inventory(**inventory_dict_test)
        for key, val in inventory_item.return_as_dictionary().items():
            self.assertEqual(val, inventory_dict_test[key], 
                             f'Comparing {key} = {val}, ' +
                             'supposed to be {key} = {inventory_dict_test[key]}')

class MarketPricesTest(TestCase):
    def test_market_price(self):
        self.assertEqual(24, get_latest_price())

class MainTest(TestCase):
    @patch('builtins.input', lambda *args: '1')
    def test_main_menu_goes_to_add_new_item(self):
        self.assertEqual(main.main_menu(), main.main_menu('1'))

    @patch('builtins.input', lambda *args: '2')
    def test_main_menu_goes_to_get_item_info(self):
        self.assertEqual(main.main_menu(), main.main_menu('2'))

    @patch('builtins.input', lambda *args: 'q')
    def test_main_menu_goes_to_quit(self):
        self.assertEqual(main.main_menu(), main.main_menu('q'))
    
    def test_get_info_of_non_existent_item(self):
        with patch('builtins.input', return_value='0'):
            main.item_info()

    def test_add_new_electric_appliance_item(self):
        with patch('builtins.input', side_effect=['1', 'phone', '400.00', 'N',
                   'Y', 'Nokia', '120V']):
            main.add_new_item()
        with patch('builtins.input', return_value='1'):
            main.item_info()

    def test_add_new_furniture_item(self):
        with patch('builtins.input', side_effect=['2', 'bed', '250.00', 'Y', 'Wood', 'L']):
            main.add_new_item()
        with patch('builtins.input', return_value='2'):
            main.item_info()

    def test_add_new_generic_item(self):
        with patch('builtins.input', side_effect=['3', 'some item', '20', 'N', 'N']):
            main.add_new_item()
        with patch('builtins.input', return_value='3'):
            main.item_info()

if __name__ == "__main__":
    unittest.main()
