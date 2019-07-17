""" Unit tests for electric appliances class """

import unittest
from inventory_management.electric_appliances_class import ElectricAppliances


class ElectricAppliancesTest(unittest.TestCase):
    """ Test the Electric Appliance class """

    def test_init(self):
        """ Test init """
        washer = ElectricAppliances(123, "washer", 500, 150, "GE", 100)
        self.assertEqual(washer.product_code, 123)
        self.assertEqual(washer.description, "washer")
        self.assertEqual(washer.market_price, 500)
        self.assertEqual(washer.rental_price, 150)
        self.assertEqual(washer.brand, "GE")
        self.assertEqual(washer.voltage, 100)

    def test_return_as_dictionary(self):
        """ Test the return as dictionary method """
        chair_dict = ElectricAppliances(123, "washer", 500, 150, "GE", 100
                                        ).return_as_dictionary()
        self.assertEqual(chair_dict['product_code'], 123)
        self.assertEqual(chair_dict['description'], "washer")
        self.assertEqual(chair_dict['market_price'], 500)
        self.assertEqual(chair_dict['rental_price'], 150)
        self.assertEqual(chair_dict['brand'], 'GE')
        self.assertEqual(chair_dict['voltage'], 100)
