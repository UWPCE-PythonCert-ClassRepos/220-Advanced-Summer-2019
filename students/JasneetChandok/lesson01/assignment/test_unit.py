""" Unit tests for inventory management """
from unittest import TestCase, mock
import unittest
from unittest.mock import patch

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


class MarketPriceTest(TestCase):
    """Test market_price module"""

    def test_get_latest_price(self):
        """Test get_latest_price function"""
        self.assertEqual(market_prices.get_latest_price(''), 24)


if __name__ == "__main__":
    unittest.main()
