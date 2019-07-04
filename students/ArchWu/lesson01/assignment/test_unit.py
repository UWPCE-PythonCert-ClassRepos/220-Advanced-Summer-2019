""" Unit tests for inventory management """
import unittest
from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances

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
