from unittest import TestCase
from unittest.mock import MagicMock
import io
import inventory_management.main as Main


class TestMain(TestCase):
    """
    Testing main
    """
    def test_main_menu(self):
        """
        testing method
        """
        self.assertEqual(Main.mainMenu('1'), Main.addNewItem)
        self.assertEqual(Main.mainMenu('2'), Main.itemInfo)
        self.assertEqual(Main.mainMenu('q'), Main.exitProgram)
        