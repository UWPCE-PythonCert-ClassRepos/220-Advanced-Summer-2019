""" Unit tests for furniture class """

import unittest
from inventory_management.furniture_class import Furniture


class FurnitureTest(unittest.TestCase):
    """ Test the Furniture class """

    def test_init(self):
        """ Test init """
        chair = Furniture(123, "chair", 100, 50, "wood", "m")
        self.assertEqual(chair.product_code, 123)
        self.assertEqual(chair.description, "chair")
        self.assertEqual(chair.market_price, 100)
        self.assertEqual(chair.rental_price, 50)
        self.assertEqual(chair.material, "wood")
        self.assertEqual(chair.size, "m")

    def test_return_as_dictionary(self):
        """ Test the return as dictionary method """
        chair_dict = Furniture(123, "chair", 100, 50, "wood", "m"
                                   ).return_as_dictionary()
        self.assertEqual(chair_dict['product_code'], 123)
        self.assertEqual(chair_dict['description'], "chair")
        self.assertEqual(chair_dict['market_price'], 100)
        self.assertEqual(chair_dict['rental_price'], 50)
        self.assertEqual(chair_dict['material'], 'wood')
        self.assertEqual(chair_dict['size'], 'm')
