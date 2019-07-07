"""unit test"""
from unittest import TestCase
from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliance_class import ElectricAppliances
from inventory_management import main


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

    def test_return_as_dictionary(self):
        """class method test"""

        result_f = self.furniture.return_as_dictionary()
        self.assertEqual("wood", result_f["material"])
        self.assertEqual("Large", result_f["size"])

        result_a = self.appliance.return_as_dictionary()
        self.assertEqual("basic", result_a["brand"])
        self.assertEqual("110V", result_a["voltage"])


if __name__ == "__main__":
    unittest.main()
