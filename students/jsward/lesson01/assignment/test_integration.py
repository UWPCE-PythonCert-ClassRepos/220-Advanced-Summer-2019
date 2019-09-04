import unittest
from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock

from inventory_management.electric_appliances import ElectricAppliances
from inventory_management.furniture import Furniture
from inventory_management.inventory import Inventory
import inventory_management.main as main
from inventory_management.main import item_info
from inventory_management import market_prices as market_price
import io


class IntegrationTests(TestCase):
    """Tests inventory_management end-to-end"""

    def mock_appliance_inputs(self, prompt):
        prompts = {
            ">": "1",
            "Enter item code: ": "0",
            "Enter item description: ": "Desc",
            "Enter item rental price: ": "0",
            "Is this item a piece of furniture? (Y/N): ": "N",
            "Is this item an electric appliance? (Y/N): ": "Y",
            "Enter item brand: ": "Generic",
            "Enter item voltage: ": "1"
        }
        return prompts[prompt]

    def mock_furniture_inputs(self, prompt):
        prompts = {
            ">": "1",
            "Enter item code: ": "1",
            "Enter item description: ": "Desc",
            "Enter item rental price: ": "0",
            "Is this item a piece of furniture? (Y/N): ": "Y",
            "Enter item material: ": "Wood",
            "Enter item size (S,M,L,XL): ": "M"
        }
        return prompts[prompt]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_integration(self, mock_stdout):

        # Add appliance item
        with patch("builtins.input", self.mock_appliance_inputs):
            main.main_menu()()
            self.assertEqual(main.full_inventory['0'], {'brand': 'Generic', 'description': 'Desc', 'market_price': 24, 'product_code': '0', 'rental_price': '0', 'voltage': '1'})

        # Add furniture item
        with patch("builtins.input", self.mock_furniture_inputs):
            main.main_menu()()
            self.assertEqual(main.full_inventory['1'], {'description': 'Desc', 'market_price': 24, 'material': 'Wood', 'product_code': '1', 'rental_price': '0', 'size': 'M'})

        # Get appliance info
        with patch("builtins.input", side_effect=["2", "0"]):
            main.main_menu()()
            mock_out_lines = mock_stdout.getvalue().split("\n")
            self.assertEqual(mock_out_lines[-2], "voltage:1")
            self.assertEqual(mock_out_lines[-3], "brand:Generic")
            self.assertEqual(mock_out_lines[-4], "rental_price:0")
            self.assertEqual(mock_out_lines[-5], "market_price:24")
            self.assertEqual(mock_out_lines[-6], "description:Desc")
            self.assertEqual(mock_out_lines[-7], "product_code:0")

        # Get furniture info
        with patch("builtins.input", side_effect=["2", "1"]):
            main.main_menu()()
            mock_out_lines = mock_stdout.getvalue().split("\n")
            self.assertEqual(mock_out_lines[-2], "size:M")
            self.assertEqual(mock_out_lines[-3], "material:Wood")
            self.assertEqual(mock_out_lines[-4], "rental_price:0")
            self.assertEqual(mock_out_lines[-5], "market_price:24")
            self.assertEqual(mock_out_lines[-6], "description:Desc")
            self.assertEqual(mock_out_lines[-7], "product_code:1")


if __name__ == "__main__":
    unittest.main()
