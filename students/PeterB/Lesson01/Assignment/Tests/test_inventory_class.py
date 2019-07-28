import unittest
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management.inventory_class import Inventory


class InventoryTest(unittest.TestCase):
    def test_init(self):
        inventory = Inventory(66, "Product", 20000, 1500)
        self.assertEqual(inventory.product_code, 66)
        self.assertEqual(inventory.description, "Product")
        self.assertEqual(inventory.market_price, 20000)
        self.assertEqual(inventory.rental_price, 1500)

    def test_return_as_dictionary(self):
        Inventory_dict = Inventory(66, "Product", 20000, 1500
                                        ).return_as_dictionary()
        self.assertEqual(Inventory_dict['product_code'], 66)
        self.assertEqual(Inventory_dict['description'], "Product")
        self.assertEqual(Inventory_dict['market_price'], 20000)
        self.assertEqual(Inventory_dict['rental_price'], 1500)