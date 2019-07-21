import unittest
from inventory_management.market_prices import*
from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances

import sys
import os

sys.path.insert(0, os.path.abspath(__file__ + "\..\inventory_management"))

#
# class demo(unittest.TestCase):
#     productCode = "A1234"
#     #inventory =
#     def test_demo(self):
#         self.assertDictEqual(
#             {"productCode" : "A1234"},
#             {"productCode": "A1234"})


class TestInventoryImplementations(unittest.TestCase):
    product_code = "abc"
    description = "myInvent"
    market_price = 100
    rental_price = 5
    material = "iron"
    size = "large"
    brand = "GE"
    voltage = 110

    def test_inventory(self):
        test_inventory = Inventory(
            self.product_code,
            self.description,
            self.market_price,
            self.rental_price)
        self.assertDictEqual(
            {"product_code": self.product_code,
             "description": self.description,
             "market_price": self.market_price,
             "rental_price": self.rental_price},
            test_inventory.return_as_dictionary())

    def test_furniture(self):
        test_furniture = Furniture(
            self.product_code,
            self.description,
            self.market_price,
            self.rental_price,
            self.material,
            self.size)
        self.assertDictEqual(
            {"product_code": self.product_code,
             "description": self.description,
             "market_price": self.market_price,
             "rental_price": self.rental_price,
             "material": self.material,
             "size": self.size},
            test_furniture.return_as_dictionary())

    def test_electric_appliance(self):
        test_electric_appliance = ElectricAppliances(
            self.product_code,
            self.description,
            self.market_price,
            self.rental_price,
            self.brand,
            self.voltage)
        self.assertDictEqual(
            {"product_code": self.product_code,
             "description": self.description,
             "market_price": self.market_price,
             "rental_price": self.rental_price,
             "brand": self.brand,
             "voltage": self.voltage},
            test_electric_appliance.return_as_dictionary()
        )

    def test_market_price(self):
        self.assertEquals(24, get_latest_price(123))
