from unittest import TestCase
from unittest.mock import patch

from electricAppliancesClass import electricAppliancesClass
import market_prices as mp
import main


class ElectricAppliancesTest(TestCase):
    def test_electrical_appliances(self):
        appliance = electricAppliances(
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            )
        self.assertDictEqual(appliance.returnAsDictionary(), appliance)

class MarketPriceTest(TestCase):
    def test_gest_latest_price(self):
        self.assertEqual(
            24,
            mp.test_gest_latest_price(180)
        )

class MainMenuTest(TestCase):
    def test_main_menu(self):
        with patch("builtins.input", side_effect=2):
            self.assertEqual(main.mainMenu(), main.ItemInfo)
