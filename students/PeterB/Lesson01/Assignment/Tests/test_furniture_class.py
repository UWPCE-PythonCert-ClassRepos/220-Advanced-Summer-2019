import unittest
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances

class FurnitureTest(unittest.TestCase):
    def test_init(self):
        Couch = Furniture(62, "Couch", 2000, 150, "Leather", "Sectional")
        self.assertEqual(Couch.product_code, 62)
        self.assertEqual(Couch.description, "Couch")
        self.assertEqual(Couch.market_price, 2000)
        self.assertEqual(Couch.rental_price, 150)
        self.assertEqual(Couch.material, "Leather")
        self.assertEqual(Couch.style, "Sectional")

    def test_return_as_dictionary(self):
        Couch_dict = Furniture(62, "Couch", 2000, 150, "Leather",
                                        "Sectional").return_as_dictionary()
        self.assertEqual(Couch_dict['product_code'], 62)
        self.assertEqual(Couch_dict['description'], "Couch")
        self.assertEqual(Couch_dict['market_price'], 2000)
        self.assertEqual(Couch_dict['rental_price'], 150)
        self.assertEqual(Couch_dict['material'], "Leather")
        self.assertEqual(Couch_dict['style'], "Sectional")