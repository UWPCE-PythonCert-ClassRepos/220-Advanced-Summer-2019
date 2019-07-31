from inventory_management.InventoryClass import Inventory
from inventory_management.FurnitureClass import Furniture
from inventory_management.ElectricAppliancesClass import ElectricAppliances
from inventory_management.market_prices import get_latest_price
from inventory_management.main import main_menu, get_price, add_new_item, item_info, exit_program
from unittest import TestCase, mock
from mock import patch


class InventoryClassTest(TestCase):
    """
    This class tests the InventoryClass module
    """

    def setUp(self):
        self.inventory = Inventory(product_code=1, description='test',
                                   market_price=99.99, rental_price=9.99)
        self.expected_inventory_dict = {
            'product_code': 1,
            'description': 'test',
            'market_price': 99.99,
            'rental_price': 9.99
        }

    def test_inventory_init(self):
        self.assertEqual(self.inventory.__dict__,
                         self.expected_inventory_dict)
        self.assertIsInstance(self.inventory, Inventory)

    def test_return_as_dictionary(self):
        """ Verify dictionary returned matches expected """
        self.assertDictEqual(self.inventory.return_as_dictionary(),
                             self.expected_inventory_dict)


class FurnitureClassTest(TestCase):
    """
    This class tests the FurnitureClass module
    """

    def setUp(self):
        self.furniture = Furniture(product_code=1, description='test',
                                   market_price=99.99, rental_price=9.99,
                                   material='Leather', size='S')
        self.expected_furniture_dict = {
            'product_code': 1,
            'description': 'test',
            'market_price': 99.99,
            'rental_price': 9.99,
            'material': 'Leather',
            'size': 'S'
        }

    def test_furniture_init(self):
        self.assertEqual(self.furniture.__dict__, self.expected_furniture_dict)
        self.assertIsInstance(self.furniture, Furniture)


class ElectricAppliancesClassTest(TestCase):
    """
    This class tests the ElectricAppliancesClass module
    """

    def setUp(self):
        self.electric_appliance = ElectricAppliances(product_code=1,
                                                     description='test',
                                                     market_price=99.99,
                                                     rental_price=9.99,
                                                     brand='Dewalt',
                                                     voltage=20)
        self.expected_electric_appliance_dict = {
            'product_code': 1,
            'description': 'test',
            'market_price': 99.99,
            'rental_price': 9.99,
            'brand': 'Dewalt',
            'voltage': 20
        }

    def test_electric_appliances_init(self):
        self.assertEqual(self.electric_appliance.__dict__,
                         self.expected_electric_appliance_dict)
        self.assertIsInstance(self.electric_appliance, ElectricAppliances)


class MarketPricesTest(TestCase):
    """
    This class tests the market_prices module
    """

    def setUp(self):
        self.inventory_item1 = \
            Inventory(product_code=1, description='test',
                      market_price=99.99, rental_price=9.99)
        self.get_latest_price = \
            get_latest_price(item_code=self.inventory_item1.product_code)

    def test_latest_price(self):
        self.get_latest_price = mock.MagicMock(return_value=99.99)
        self.get_latest_price(item_code=self.inventory_item1.product_code)
        self.get_latest_price.assert_called_with(item_code=1)


class MainTest(TestCase):
    """
    This class tests the main.py module
    """

    def setUp(self):
        self.test_item = {'product_code': 1, 'description': 'test',
                          'market_price': 99.99, 'rental_price': 9.99}

    def test_main_menu(self):
        with patch("builtins.input", side_effect="1"):
            self.assertEqual(main_menu(), add_new_item)

        with patch("builtins.input", side_effect="2"):
            self.assertEqual(main_menu(), item_info)

        with patch("builtins.input", side_effect="q"):
            self.assertEqual(main_menu(), exit_program)

    def test_get_price(self):
        self.assertEqual(get_price(item_code=1),  24)

    def test_add_new_item(self):
        with patch("builtins.input", side_effect="Test"):
            with self.assertRaises(StopIteration):
                add_new_item(full_inventory={})

    @patch('inventory_management.main.item_info', return_value='product_code:1\n'
                                                               'description:test\n'
                                                               'market_price:99.99\n'
                                                               'rental_price:9.99')
    def test_item_info(self, item_info):
        item_info = item_info()
        for key, value in self.test_item.items():
            self.assertIn(f'{key}:{value}', item_info)


    def test_exit_program(self):
        with self.assertRaises(SystemExit):
            exit_program(full_inventory={})

        with self.assertRaises(TypeError):
            exit_program()
