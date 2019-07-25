"""Integration test"""
import unittest
from inventory_management.inventory_class import Inventory
from inventory_management.furniture_class import Furniture
from inventory_management.electric_appliances_class import ElectricAppliances
from inventory_management import main
from inventory_management import market_prices
from unittest import TestCase, mock

class MainTest(unittest.TestCase):
    """Test main module"""
    def test_main(self):
        """Test main_menu function """
        with mock.patch('builtins.input',
                        side_effect=['1', '1', '2', '3', 'n', 'y', '4', '5']):
            main.main_menu()
            self.assertEqual(main.FULL_INVENTORY['1']['product_code'], '1')
            self.assertEqual(main.FULL_INVENTORY['1']['market_price'], 24)
            self.assertEqual(main.FULL_INVENTORY['1']['brand'], '4')
            self.assertEqual(main.FULL_INVENTORY['1']['voltage'], '5')
        with mock.patch('builtins.input',
                        side_effect=['2', '2', '3', 'n', 'n', '4', '5']):
            main.main_menu('1')
            self.assertEqual(main.FULL_INVENTORY['2']['product_code'], '2')
            self.assertEqual(main.FULL_INVENTORY['2']['market_price'], 24)
        with mock.patch('builtins.input',
                        side_effect=['3', '2', '3', 'y', '4', '5']):
            main.main_menu('1')
            self.assertEqual(main.FULL_INVENTORY['3']['product_code'], '3')
            self.assertEqual(main.FULL_INVENTORY['3']['market_price'], 24)
            self.assertEqual(main.FULL_INVENTORY['3']['material'], '4')
            self.assertEqual(main.FULL_INVENTORY['3']['size'], '5')
        with mock.patch('builtins.input',
                        side_effect=['q', '2', '3', 'y', '4', '5']):
            with self.assertRaises(SystemExit):
                main.main_menu()
                self.assertRaises(SystemExit, main.exit_program())
        with mock.patch('builtins.input',
                        side_effect=['2', '2', '3', 'y', '4', '5']):
            main.main_menu()
            self.assertEqual(main.FULL_INVENTORY['3']['product_code'], '3')
            self.assertEqual(main.FULL_INVENTORY['3']['market_price'], 24)
            self.assertEqual(main.FULL_INVENTORY['3']['material'], '4')
            self.assertEqual(main.FULL_INVENTORY['3']['size'], '5')

if __name__ == "__main__":
    unittest.main()
