from unittest import TestCase
from mock import MagicMock

from inventoryClass import inventory
from electricAppliancesClass import electricAppliances
from furnitureClass import furniture


class InventoryTests(TestCase):
    def test_inventory(self):
        try:
            test_inventory_init = inventory.__init__(self, 42, 'goat', 200, 50)
        except TypeError:
            ('Missing posistional requirements.')
        self.assertIsNone(test_inventory_init, msg=None)

        test_inventory_dict = inventory.returnAsDictionary(self)
        self.assertIsNotNone(test_inventory_dict, msg=None)
        self.assertIs(42, test_inventory_dict['productCode'])

        for values in test_inventory_dict.items():
                self.assertIs(42, test_inventory_dict['productCode'])
                self.assertIs('goat', test_inventory_dict['description'])
                self.assertIs(200, test_inventory_dict['marketPrice'])
                self.assertIs(50, test_inventory_dict['rentalPrice'])


class ElectricAppliancesTests(TestCase):
    def test_electric_appliances(self):
        test_electric_appliances_init = electricAppliances.__init__(self, 42, 'goat', 200, 50, 'Samsung', '220v')
        test_electric_appliances_dict = electricAppliances.returnAsDictionary(self)

        for values in test_electric_appliances_dict.values():
            self.assertIs(42, test_electric_appliances_dict['productCode'])
            self.assertIs('goat', test_electric_appliances_dict['description'])
            self.assertIs(200, test_electric_appliances_dict['marketPrice'])
            self.assertIs(50, test_electric_appliances_dict['rentalPrice'])
            self.assertIs('Samsung', test_electric_appliances_dict['brand'])
            self.assertIs('220v', test_electric_appliances_dict['voltage'])


class FurnitureTests(TestCase):
    def test_furniture(self):
        test_furnitire_init = furniture.__init__(self, 42, 'goat', 200, 50, 'leather', 'medium')
        test_furniture_dict = furniture.returnAsDictionary(self)
        self.assertIsNotNone(test_furniture_dict)

        for values in test_furniture_dict.values():
            self.assertIs(42, test_furniture_dict['productCode'])
            self.assertIs('goat', test_furniture_dict['description'])
            self.assertIs(200, test_furniture_dict['marketPrice'])
            self.assertIs(50, test_furniture_dict['rentalPrice'])
            self.assertIs('leather', test_furniture_dict['material'])
            self.assertIs('medium', test_furniture_dict['size'])
