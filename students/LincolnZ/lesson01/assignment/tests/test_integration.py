from unittest import TestCase
from unittest.mock import patch
from inventory_management import main


class test_integraty(TestCase):
    """setup the test"""

    @staticmethod
    def test_add_new_generic_item():
        with patch('builtins.input', side_effect=['100', 'inventory', 15, 'N', 'N']):
            main.add_new_item()

    @staticmethod
    def test_add_new_furniture_item():
        with patch('builtins.input', side_effect=['200', 'test chair', 25, 'Y', 'Wood', 'L']):
            main.add_new_item()

    @staticmethod
    def test_add_new_electric_appliance_item():
        with patch('builtins.input', side_effect=['300', 'test lamp', 35, 'N', 'Y', 'basic', '110V']):
            main.add_new_item()

    def test_full_inventory(self):
        """assert full inventory item"""

        self.assertDictEqual(main.FULL_INVENTORY['100'], {"product_code": "100", "description": "inventory",
                                                          "market_price": 24,
                                                          "rental_price": 15})

        self.assertDictEqual(main.FULL_INVENTORY['200'], {"product_code": "200", "description": "test chair",
                                                          "market_price": 24,
                                                          "rental_price": 25,
                                                          "material": "Wood",
                                                          "size": "L"})

        self.assertDictEqual(main.FULL_INVENTORY['300'], {"product_code": "300", "description": "test lamp",
                                                          "market_price": 24,
                                                          "rental_price": 35,
                                                          "brand": "basic",
                                                          "voltage": "110V"})

