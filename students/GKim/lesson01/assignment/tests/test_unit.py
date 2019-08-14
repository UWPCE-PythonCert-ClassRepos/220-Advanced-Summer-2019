"""
test unit module
"""

from unittest import TestCase
from unittest.mock import MagicMock, patch
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management.furniture_class import Furniture
from inventory_management.inventory_class import Inventory
from inventory_management import market_prices
from inventory_management.main import main

class ElectricApplianceTest(TestCase):
    """
    EA class
    """
    def test_return_dictionary(self):
        """
        Dictionary output
        """
        appliance = ElectricAppliances("A", "B", "C", "D", "E", "F")

        self.assertDictEqual(
            {
                "product_code": "A",
                "description": "B",
                "market_price": "C",
                "rental_price": "D",
                "brand": "E",
                "voltage": "F",
            }, appliance.return_as_dictionary()
        )

class FurnitureTest(TestCase):
    """
    Furniture Class
    """
    def test_return_dictionary(self):
        """
        Dictionary output
        """
        furn = Furniture("A", "B", "C", "D", "E", "F")
        self.assertDictEqual(
            {
                "product_code": "A",
                "description": "B",
                "market_price": "C",
                "rental_price": "D",
                "material": "E",
                "size": "F",
            }, furn.return_as_dictionary()
        )


class InventoryTest(TestCase):
    """
    Inventory Class
    """
    def test_return_dictionary(self):
        """
        dictionary output
        """
        inv = Inventory("A", "B", "C", "D")
        self.assertDictEqual(
            {
                "product_code": "A",
                "description": "B",
                "market_price": "C",
                "rental_price": "D",
            }, inv.return_as_dictionary()
        )

class MarketPriceTest(TestCase):
    """
    Market Price Class
    """
    def test_get_latest_prices(self):
        """
        get price method
        """
        self.assertEqual(24, market_prices.get_latest_price(100))


class MainMenuTest(TestCase):
    def test_main_menu(self):
        with patch("builtin.input", side_effect="2"):
            self.assertEqual(main.main_menu(), main.item_info())








