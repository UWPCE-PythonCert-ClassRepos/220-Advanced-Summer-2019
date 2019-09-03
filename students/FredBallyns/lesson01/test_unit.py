import sys
sys.path.insert(0, './inventory_management')

import unittest
import inventory_class
import furniture_class
import electric_appliances_class
import market_prices
import main
from unittest.mock import patch, call


class InventoryClassTest(unittest.TestCase):

    def test_return_as_dict(self):
        inventory_item = inventory_class.Inventory(555, 'item_555', 10.00, 2.00)
        inventory_test_dict = {
            'product_code': 555,
            'description': 'item_555',
            'market_price': 10.00,
            'rental_price': 2.00}

        for k, val in inventory_item.return_as_dictionary().items():
            self.assertEqual(val, inventory_test_dict[k],
                f'Comparing {k} = {val}, supposed to be {k} = {inventory_test_dict[k]}')


class FurnitureClassTest(unittest.TestCase):

    def test_return_as_dict(self):
        furniture_item = furniture_class.Furniture(444, 'item_444', 0.99, 0.05, 'air', 'small')
        furniture_test_dict = {
            'product_code': 444,
            'description': 'item_444',
            'market_price': 0.99,
            'rental_price': 0.05,
            'material': "air",
            'size': 'small'}
        for k, val in furniture_item.return_as_dictionary().items():
            self.assertEqual(val, furniture_test_dict[k],
                             f'Comparing {k} = {val}, supposed to be {k} = {furniture_test_dict[k]}')


class ElectricAppliancesTest(unittest.TestCase):

    def test_return_as_dict(self):
        electric_item = electric_appliances_class.ElectricAppliances(666, 'item_666', 1234.56, 78.90, 'GE', '21 GW')
        electric_test_dict = {
            'product_code': 666,
            'description': 'item_666',
            'market_price': 1234.56,
            'rental_price': 78.90,
            'brand': 'GE',
            'voltage': "21 GW"}
        for k, val in electric_item.return_as_dictionary().items():
            self.assertEqual(val, electric_test_dict[k],
                             f'Comparing {k} = {val}, supposed to be {k} = {electric_test_dict[k]}')


class MarketPriceTest(unittest.TestCase):

    def test_market_price(self):
        val = 24
        self.assertEqual(val,market_prices.get_latest_price("item_code1"),
                         f'{val} is equal to {market_prices.get_latest_price("item_code1")}')
        self.assertEqual(val,market_prices.get_latest_price(""),
                         f'{val} is equal to {market_prices.get_latest_price("")}')


class MainTest(unittest.TestCase):

    def test_main_menu(self):
        with patch('builtins.input', side_effect="1"):
            self.assertEqual(main.main_menu(), main.add_new_item)
        with patch('builtins.input', side_effect=["error_input", "1"]):
            self.assertEqual(main.main_menu(), main.add_new_item)
        with patch("builtins.input", side_effect="2"):
            self.assertEqual(main.main_menu(), main.item_info)
        with patch("builtins.input", side_effect="q"):
            self.assertEqual(main.main_menu(), main.exit_program)
        with patch("builtins.input", side_effect=["zzzz", "q"]):
            self.assertEqual(main.main_menu(), main.exit_program)

    def test_get_price(self):
            self.assertEqual(main.get_price('itemcode123'), 24)
            self.assertEqual(main.get_price(''), 24)

    @staticmethod
    def test_add_new_furniture_item():
        with patch('builtins.input', side_effect=['1', 'furn', '100', "y", 'wood', 'small']):
            main.add_new_item()
            furniture_expected = {'product_code': '1', 'description': 'furn', 'market_price': 24, 'rental_price': '100', 'material': 'wood', 'size': 'small'}
            assert(main.FULL_INVENTORY['1']==furniture_expected)

    @staticmethod
    def test_add_new_electric_appliance_item():
        with patch('builtins.input', side_effect=['2', 'elec', '200', "n", "y", 'GE', '21 GW']):
            main.add_new_item()
            electric_expected = {'product_code': '2', 'description': 'elec', 'market_price': 24, 'rental_price': '200', 'brand': 'GE', 'voltage': "21 GW"}
            assert(main.FULL_INVENTORY['2']==electric_expected)

    @staticmethod
    def test_add_new_inventory_item():
        with patch('builtins.input', side_effect=['3', 'inven', '300', "n", "n"]):
            main.add_new_item()
            inventory_expected = {'product_code': '3', 'description': 'inven', 'market_price': 24, 'rental_price': '300'}
            assert(main.FULL_INVENTORY['3']==inventory_expected)

    def test_item_info(self):
        with patch('builtins.input', side_effect=['3', 'inven', '1', "n", "n"]):
            main.add_new_item()
        with patch('builtins.input', side_effect=['not_there']):
            with patch('sys.stdout') as test_stdout:
                main.item_info()
                test_stdout.assert_has_calls(
                    [call.write("Item not found in inventory"),
                     call.write("\n")])
        with patch('builtins.input',  side_effect=['3']):
            with patch('sys.stdout') as test_stdout:
                main.item_info()
                test_stdout.assert_has_calls(
                    [call.write('product_code:3'),
                     call.write('\n'),
                     call.write('description:inven'),
                     call.write('\n'),
                     call.write('market_price:24'),
                     call.write('\n'),
                     call.write('rental_price:1'),
                     call.write('\n')])

    def test_exit_program(self):
        with self.assertRaises(SystemExit):
            self.assertRaises(SystemExit, main.exit_program())

if __name__ == "__main__":
    unittest.main()