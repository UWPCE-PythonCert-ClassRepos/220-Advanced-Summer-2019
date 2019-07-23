"""unit test"""
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import MagicMock
from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliance_class import ElectricAppliances
from inventory_management import main
from inventory_management import market_prices


class inventory_test(TestCase):
    """unit test for inventory and its sub classes"""

    def setUp(self):
        """set up instance of each sub class"""
        self.furniture = Furniture(100, "test chair",
                                   20, (1.5, "day"),
                                   "wood", "Large")

        self.appliance = ElectricAppliances(200, "test lamp",
                                            30, (2.5, "day"),
                                            "basic", "110V")
        self.appliance_expected_output = {
                                            "product_code": 200,
                                            "description": "test lamp",
                                            "market_price": 30,
                                            "rental_price": (2.5, "day"),
                                            "brand": "basic",
                                            "voltage": "110V",
                                            }
        self.furniture_expected_output = {
                                            "product_code": 100,
                                            "description": "test chair",
                                            "market_price": 20,
                                            "rental_price": (1.5, "day"),
                                            "material": "wood",
                                            "size": "Large",
                                            }

    def test_electric_appliances(self):

        self.assertDictEqual(self.appliance.return_as_dictionary(), self.appliance_expected_output)

    def test_furniture(self):

        self.assertDictEqual(self.furniture.return_as_dictionary(), self.furniture_expected_output)


class test_market_price(TestCase):

    def test_get_latest_price_mock(self):
        """a mock test"""
        market_prices.get_latest_price = MagicMock(return_value=3)
        market_prices.get_latest_price()
        market_prices.get_latest_price.assert_called()
        market_prices.get_latest_price.assert_called_once()
        self.assertEqual(3, market_prices.get_latest_price())

    def test_get_latest_price_patch_a(self):
        """a patch test as context manager"""
        with patch("market_prices.get_latest_price") as mocked_get_price:
            market_prices.get_latest_price()
            mocked_get_price.assert_called()
            mocked_get_price.assert_called_once()

    @patch('market_prices.get_latest_price')
    def test_get_latest_price_patch_b(self, mocked_get_price):
        """a patch test as decorator"""

        market_prices.get_latest_price()
        mocked_get_price.assert_called()
        mocked_get_price.assert_called_once()


class test_main(TestCase):
    """unit test for main.py"""

    """ This class handles test cases for the main test file """

    @patch('builtins.input', lambda *args: '1')
    def test_main_menu_goes_to_add_new_item(self):
        self.assertEqual(main.main_menu(), main.main_menu('1'))

    @patch('builtins.input', lambda *args: '2')
    def test_main_menu_goes_to_get_item_info(self):
        self.assertEqual(main.main_menu(), main.main_menu('2'))

    @patch('builtins.input', lambda *args: 'q')
    def test_main_menu_goes_to_quit(self):
        self.assertEqual(main.main_menu(), main.main_menu('q'))

    def test_get_price_of_item(self):
        self.assertEqual(main.get_price(), 24)

    def test_get_info_of_non_existent_item(self):
        with patch('builtins.input', return_value='0'):
            main.item_info()

    def test_get_info_of_item(self):
        with patch('builtins.input', side_effect=['1', 'fake', '100', 'N', 'N']):
            main.add_new_item()
        with patch('builtins.input', return_value='1'):
            main.item_info()

    # def test_sys_exit(self):
    #     with patch("")

    @staticmethod
    def test_add_new_generic_item():
        with patch('builtins.input', side_effect=['2', 'fake', '100', 'N', 'N']):
            main.add_new_item()

    @staticmethod
    def test_add_new_furniture_item():
        with patch('builtins.input', side_effect=['3', 'fake', '100', 'Y', 'Wool', 'L']):
            main.add_new_item()

    @staticmethod
    def test_add_new_electric_appliance_item():
        with patch('builtins.input', side_effect=['4', 'fake', '100', 'Y', 'GE', '120V']):
            main.add_new_item()


if __name__ == "__main__":
    unittest.main()
