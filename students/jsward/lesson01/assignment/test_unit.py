import unittest
from unittest import TestCase
from unittest.mock import patch

from inventory_management.electric_appliances import ElectricAppliances
from inventory_management.furniture import Furniture
from inventory_management.inventory import Inventory
import inventory_management.main as main
from inventory_management import market_prices as market_price
import io

# PYTHONPATH=inventory_management/ python -m unittest test_unit
# PYTHONPATH=inventory_management/ python3 -m coverage run --source=inventory_management/ -m unittest test_unit.py


class ElectricApplianceTest(TestCase):
    """Tests the ElectricAppliances class"""
    def test_electric_appliances(self):
        appliance = ElectricAppliances("A", "B", "C", "D", "E", "F")
        self.assertDictEqual(appliance.return_as_dictionary(),
            {
                'product_code': "A",
                'description': "B",
                'market_price': "C",
                'rental_price': "D",
                'brand': "E",
                'voltage': "F",
            }
        )


class FurnitureTest(TestCase):
    """Tests the Furniture class"""
    def test_furniture(self):
        furniture = Furniture("PC", "Desc", "MP", "RP", "M", "S")
        self.assertDictEqual(furniture.return_as_dictionary(),
            {
                'product_code': "PC",
                'description': "Desc",
                'market_price': "MP",
                'rental_price': "RP",
                'material': "M",
                'size': "S"
            }
        )


class InventoryTest(TestCase):
    """Tests the Inventory class"""
    def test_Inventory(self):
        inventory = Inventory("PC", "Desc", "MP", "RP")
        self.assertDictEqual(inventory.return_as_dictionary(),
            {
                'product_code': "PC",
                'description': "Desc",
                'market_price': "MP",
                'rental_price': "RP"
            }
        )


class MainMenuTest(TestCase):
    """Tests code in main.py"""

    def test_main_menu(self):
        with patch("builtins.input", side_effect="2"):
            self.assertEqual(main.main_menu(), main.item_info)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_pricec(self, mock_stdout):
        main.get_price()
        self.assertEqual(mock_stdout.getvalue(), "Get price\n")

    def test_exit_program(self):
        with self.assertRaises(SystemExit):
            main.exit_program()


class MainAddNewItemTestAppliance(TestCase):
    """Tests adding appliance via main.main_menu"""
    def setUp(self):
       main.full_inventory = {}

    def mock_appliance_inputs(self, prompt):
        prompts = {
            "Enter item code: ": "0",
            "Enter item description: ": "Desc",
            "Enter item rental price: ": "0",
            "Is this item a piece of furniture? (Y/N): ": "N",
            "Is this item an electric appliance? (Y/N): ": "Y",
            "Enter item brand: ": "Generic",
            "Enter item voltage: ": "1"
        }
        return prompts[prompt]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_new_appliance(self, mock_stdout):
        with patch('builtins.input', self.mock_appliance_inputs):
            main.add_new_item()
            self.assertEqual(main.full_inventory, {"0": {'brand': 'Generic', 'description': 'Desc', 'market_price': 24, 'product_code': '0', 'rental_price': '0', 'voltage': '1'}})
            self.assertEqual(mock_stdout.getvalue(), "New inventory item added\n")


class MainAddNewItemTestFurniture(TestCase):
    """Tests adding furniture via main.main_menu"""
    def setUp(self):
        main.full_inventory = {}

    def mock_furniture_inputs(self, prompt):
        prompts = {
            "Enter item code: ": "1",
            "Enter item description: ": "Desc",
            "Enter item rental price: ": "0",
            "Is this item a piece of furniture? (Y/N): ": "Y",
            "Enter item material: ": "Wood",
            "Enter item size (S,M,L,XL): ": "M"
        }
        return prompts[prompt]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_new_furniture(self, mock_stdout):
        with patch('builtins.input', self.mock_furniture_inputs):
            main.add_new_item()
            self.assertEqual(main.full_inventory, {"1": {'description': 'Desc', 'market_price': 24, 'material': 'Wood','product_code': '1', 'rental_price': '0', 'size': 'M'}})
            self.assertEqual(mock_stdout.getvalue(), "New inventory item added\n")


class MainItemInfoTestNotExists(TestCase):
    """Tests looking up item info that doesn't exist via main.main_menu"""
    def setUp(self):
        main.full_inventory = {}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_item_info_not_found(self, mock_stdout):
        with patch("builtins.input", side_effect="08304815"):
            main.item_info()
            self.assertEqual(mock_stdout.getvalue(), "Item not found in inventory\n")


class MainItemInfoTestExists(TestCase):
    """Tests looking up item info that exists via main.main_menu"""
    def setUp(self):
        main.full_inventory = {"0": {"A": "A"}}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_item_info_found(self, mock_stdout):
        with patch("builtins.input", side_effect="0"):
            main.item_info()
            self.assertEqual(mock_stdout.getvalue(), "A:A\n")


class MarketPricesTest(TestCase):
    """Tests the get_latest_price function"""
    def test_get_latest_price(self):
        self.assertEqual(24, market_price.get_latest_price(180))


if __name__ == "__main__":
    unittest.main()