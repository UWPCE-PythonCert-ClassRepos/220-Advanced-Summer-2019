import unittest
from inventory_management.electric_appliances_class import ElectricAppliances



class testElectricAppliances(unittest.TestCase):
    def test_init(self):
        oven = ElectricAppliances(60, "oven", 1800, 60, "ShittyOven", 66)
        self.assertEqual(oven.product_code, 60)
        self.assertEqual(oven.description, "oven")
        self.assertEqual(oven.market_price, 1800)
        self.assertEqual(oven.rental_price, 60)
        self.assertEqual(oven.brand, "ShittyOven")
        self.assertEqual(oven.voltage, 66)

    def test_return_as_dictionary(self):
        oven_dict = ElectricAppliances(60, "oven", 1800, 60, "ShittyOven", 66
                                       ).return_as_dictionary()
        self.assertEqual(oven_dict['product_code'], 60)
        self.assertEqual(oven_dict['description'], "oven")
        self.assertEqual(oven_dict['market_price'], 1800)
        self.assertEqual(oven_dict['rental_price'], 60)
        self.assertEqual(oven_dict['brand'], "ShittyOven")
        self.assertEqual(oven_dict['voltage'], 66)