from unittest  import TestCase
from

class ElectricAppliancesTest(TestCase):
    def test_electrical_app(self):
        appliance = electricAppliances(
            "A",
            "B",
            "C"
            "D",
            "E",
            "F",
        )
        self.assertDictEqual(
            appliance.returnAsDictionary(),
            {
                ['product'] = "A",
                ['description'] = "B",
                ['marketPrice'] = "C",
                ['rentalPrice'] = "D",
                ['brand'] = "E",
                ['voltage'] = "F"
            }
        )



Class MarketPriceTest(TestCase)
    def test_get_latest_price(self):
        self.assertEqual(
            24,
            mp.get_latest_price(180)
        )

class MainMenuTest(TestCase):
    def test_main_menu(self):
        with patch("bullitins.input", side_effects="2"):
            self.assertEqual(main.mainMenu(), main.itemInfo)