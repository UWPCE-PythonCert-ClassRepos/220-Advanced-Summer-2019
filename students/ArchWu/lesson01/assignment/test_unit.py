""" Unit tests for inventory management """
from unittest import TestCase, mock
import unittest

from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management import main
from inventory_management import market_prices

class InventoryTest(unittest.TestCase):
    """test Inventory class"""
    def test_init(self):
        """test init function of class"""
        test_obj = Inventory(1, 2, 3, 4)
        self.assertEqual(test_obj.product_code, 1)
        self.assertEqual(test_obj.description, 2)
        self.assertEqual(test_obj.market_price, 3)
        self.assertEqual(test_obj.rental_price, 4)

    def test_return_dict(self):
        """test return as dict function"""
        test_obj = Inventory(1, 2, 3, 4).return_as_dictionary()
        self.assertEqual(test_obj['product_code'], 1)
        self.assertEqual(test_obj['description'], 2)
        self.assertEqual(test_obj['market_price'], 3)
        self.assertEqual(test_obj['rental_price'], 4)

class FurnitureTest(unittest.TestCase):
    """Test Furniture class"""
    def test_init(self):
        """Test init"""
        test_obj = Furniture(1, 2, 3, 4, 5, 6)
        self.assertEqual(test_obj.product_code, 1)
        self.assertEqual(test_obj.description, 2)
        self.assertEqual(test_obj.market_price, 3)
        self.assertEqual(test_obj.rental_price, 4)
        self.assertEqual(test_obj.material, 5)
        self.assertEqual(test_obj.size, 6)

    def test_return_dict(self):
        """Test return as dict func"""
        test_obj = Furniture(1, 2, 3,
                             4, 5, 6).return_as_dictionary()
        self.assertEqual(test_obj['product_code'], 1)
        self.assertEqual(test_obj['description'], 2)
        self.assertEqual(test_obj['market_price'], 3)
        self.assertEqual(test_obj['rental_price'], 4)
        self.assertEqual(test_obj['material'], 5)
        self.assertEqual(test_obj['size'], 6)

class ElectricAppliancesTest(unittest.TestCase):
    """Test EA class"""
    def test_init(self):
        """Test __init__()"""
        test_obj = ElectricAppliances(1, 2, 3, 4, 5, 6)
        self.assertEqual(test_obj.product_code, 1)
        self.assertEqual(test_obj.description, 2)
        self.assertEqual(test_obj.market_price, 3)
        self.assertEqual(test_obj.rental_price, 4)
        self.assertEqual(test_obj.brand, 5)
        self.assertEqual(test_obj.voltage, 6)
    def test_return_dict(self):
        """Test return as dict func"""
        test_obj = ElectricAppliances(1, 2, 3,
                                      4, 5, 6).return_as_dictionary()
        self.assertEqual(test_obj['product_code'], 1)
        self.assertEqual(test_obj['description'], 2)
        self.assertEqual(test_obj['market_price'], 3)
        self.assertEqual(test_obj['rental_price'], 4)
        self.assertEqual(test_obj['brand'], 5)
        self.assertEqual(test_obj['voltage'], 6)

class MainTest(unittest.TestCase):
    """Test main module"""
    def test_main(self):
        """Test main_menu function """
        with mock.patch('builtins.input', side_effect=['0', 'q']):
            with mock.patch('sys.stdout'):
                with self.assertRaises(SystemExit):
                    main.main_menu()
                    mock.call.write(
                        "Please choose from the following options (1, 2, q)"
                        ).assert_called_once()
                    self.assertRaises(SystemExit, main.exit_program())

    @mock.patch('main.market_prices.get_latest_price', return_value=25)
    def test_add_new_item(self, mocked_get_latest_price):
        """Test add_new_item function """
        with mock.patch('builtins.input', return_value='n'):
            main.add_new_item()
            self.assertEqual(main.FULL_INVENTORY['n']['product_code'], 'n')
            self.assertEqual(main.FULL_INVENTORY['n']['market_price'], 25)
            mocked_get_latest_price.assert_called_once()
        with mock.patch('builtins.input', return_value='y'):
            main.add_new_item()
            self.assertEqual(main.FULL_INVENTORY['y']['product_code'], 'y')
            self.assertEqual(main.FULL_INVENTORY['y']['market_price'], 25)
            self.assertEqual(main.FULL_INVENTORY['y']['size'], 'y')
            self.assertEqual(main.FULL_INVENTORY['y']['material'], 'y')

        with mock.patch('builtins.input',
                        side_effect=['1', '2', '3', 'n', 'y', '4', '5']):
            main.add_new_item()
            self.assertEqual(main.FULL_INVENTORY['1']['product_code'], '1')
            self.assertEqual(main.FULL_INVENTORY['1']['market_price'], 25)
            self.assertEqual(main.FULL_INVENTORY['1']['brand'], '4')
            self.assertEqual(main.FULL_INVENTORY['1']['voltage'], '5')

    def test_item_info(self):
        """Test item info function"""
        with mock.patch('builtins.input', return_value='0'):
            with mock.patch('sys.stdout') as fake_stdout:
                main.item_info()
                fake_stdout.assert_has_calls(
                    [mock.call.write("Item not found in inventory"),
                     mock.call.write("\n")])
        with mock.patch('builtins.input', return_value='n'):
            with mock.patch('sys.stdout') as fake_stdout:
                main.item_info()
                fake_stdout.assert_has_calls(
                    [mock.call.write('product_code:n'),
                     mock.call.write('\n'),
                     mock.call.write('description:n'),
                     mock.call.write('\n'),
                     mock.call.write('market_price:25'),
                     mock.call.write('\n'),
                     mock.call.write('rental_price:n'),
                     mock.call.write('\n')])

    def test_get_price(self):
        """Test get_price function"""
        with mock.patch('sys.stdout') as fake_stdout:
            main.get_price('n') # A dummy input
            fake_stdout.assert_has_calls(
                [mock.call.write("Get price"),
                 mock.call.write("\n")])

    def test_exit_program(self):
        """Test exit_program function"""
        with self.assertRaises(SystemExit):
            self.assertRaises(SystemExit, main.exit_program())

class MarketPriceTest(TestCase):
    """Test market_price module"""
    def test_get_latest_price(self):
        """Test get_latest_price function"""
        self.assertEqual(market_prices.get_latest_price(''), 24)

if __name__ == "__main__":
    unittest.main()
