""" Unit tests for inventory management """
from unittest import TestCase, mock
import unittest

from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management import main

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
        self.assertEqual(main.main_menu('1'), main.add_new_item)
        self.assertEqual(main.main_menu('2'), main.item_info)
        self.assertEqual(main.main_menu('q'), main.exit_program)

    @mock.patch("main.market_prices", return_value=24)
    def test_add_new_item(self, mocked_market_prices):
        """Test add_new_item function """
        with mock.patch('builtins.input', return_value='n'):
            main.add_new_item()
            self.assertEqual(main.FULL_INVENTORY['n']['product_code'], 'n')
            self.assertEqual(main.FULL_INVENTORY['n']['market_price'], 24)
            mocked_market_prices.get_latest_price.assert_called_once()

    def test_item_info(self):
        """Test item info function"""
