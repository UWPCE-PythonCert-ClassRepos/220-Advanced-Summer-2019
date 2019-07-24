""" Unit tests for furniture class """

import unittest
from inventory_management.inventory_class import Inventory


class FurnitureTest(unittest.TestCase):
    """ Test the Furniture class """

    def test_init(self):
        """ Test init """
        inventory = Inventory(123, "product", 10, 5)
        self.assertEqual(inventory.product_code, 123)
        self.assertEqual(inventory.description, "product")
        self.assertEqual(inventory.market_price, 10)
        self.assertEqual(inventory.rental_price, 5)

    def test_return_as_dictionary(self):
        """ Test the return as dictionary method """
        inventory_dict = Inventory(123, "product", 10, 5).return_as_dictionary()
        self.assertEqual(inventory_dict['product_code'], 123)
        self.assertEqual(inventory_dict['description'], "product")
        self.assertEqual(inventory_dict['market_price'], 10)
        self.assertEqual(inventory_dict['rental_price'], 5)
