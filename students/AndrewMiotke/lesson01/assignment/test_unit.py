""" Unit tests for inventory management """

import unittest
from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliance_class import ElectricAppliances

class InventoryTest(unittest.TestCase):
    """ Test the Inventory class """

    def test_init(self):
        """ Test init """

        test_inventory = Inventory(123, "chair", 100, 50)

        self.assertEqual(test_inventory.product_code, 123)
        self.assertEqual(test_inventory.description, "chair")
        self.assertEqual(test_inventory.market_price, 100)
        self.assertEqual(test_inventory.rental_price, 50)


    def test_return_as_dictionary(self):
        """ Test the return as dictionary method """

        test_inventory = Inventory(123, "chair", 100, 50).return_as_dictionary()

        self.assertEqual(test_inventory['product_code'], 123)
        self.assertEqual(test_inventory['description'], "chair")
        self.assertEqual(test_inventory['market_price'], 100)
        self.assertEqual(test_inventory['rental_price'], 50)


class FurnitureTest(Inventory, unittest.TestCase):
    """ Test the Furniture class """

    def test_init(self):
        """ Test init """

        test_inventory = Furniture(123, "chair", 100, 50, "wood", "m")

        self.assertEqual(test_inventory.material, "wood")
        self.assertEqual(test_inventory.size, "m")


    def test_return_as_dictionary(self):
        """ Test the return as dictionary method """

        test_inventory = Furniture(123,
                                   "chair",
                                   100,
                                   50,
                                   "wood",
                                   "m").return_as_dictionary()

        self.assertEqual(test_inventory['material'], 'wood')
        self.assertEqual(test_inventory['size'], 'm')



class ElectricTest(unittest.TestCase):
    """ Test the Electrical class """

    def test_init(self):
        """ Test init """

        test_inventory = ElectricAppliances(123, "chair", 100, 50, "GE", 75)

        self.assertEqual(test_inventory.brand, "GE")
        self.assertEqual(test_inventory.voltage, 75)


    def test_return_as_dictionary(self):
        """ Test the return as dictionary method """

        test_inventory = ElectricAppliances(123,
                                            "chair",
                                            100,
                                            50,
                                            "GE",
                                            75).return_as_dictionary()

        self.assertEqual(test_inventory['brand'], 'GE')
        self.assertEqual(test_inventory['voltage'], 75)


if __name__ == '__main__':
    unittest.main()
