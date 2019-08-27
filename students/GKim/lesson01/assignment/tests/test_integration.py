import unittest
from unittest import mock
from unittest import TestCase
import io
import inventory_management.Main as Main


class TestMain(TestCase):
    """
    Contains unit tests for Main.py
    """

    def test_main_menu(self):
        """
        Test the main menus functionality. Ensures
        correct functions are called when provided input
        :return: None
        """

        # Tests to verify the main menu will call the correct functions
        self.assertEqual(Main.main_menu('1'), Main.add_new_item)
        self.assertEqual(Main.main_menu('2'), Main.item_info)
        self.assertEqual(Main.main_menu('q'), Main.exit_program)

        # Create Patches at instances of 'input()' functions
        # ensures the patched input functions will direct to the
        # Correct associated functions.
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.assertEqual(Main.main_menu(), Main.add_new_item)
        with unittest.mock.patch('builtins.input', return_value='2'):
            self.assertEqual(Main.main_menu(), Main.item_info)
        with unittest.mock.patch('builtins.input', return_value='q'):
            self.assertEqual(Main.main_menu(), Main.exit_program)

    def test_exit_program(self):
        """
        Tests the Exit Program functionality of Main.py
        Ensures function will exit program when called.
        :return: None
        """

        # Ensures System Exit Is Raised WHen Program is Exited.
        with self.assertRaises(SystemExit):
            Main.exit_program()

    def test_get_price(self):
        """
        Tests get Price Method of Main.py
        Ensures the price will be returned when called
        :return: None
        """
        # Create patch to handle each instance of print
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            Main.get_price()

        # Obtain StringIO output from get price
        fake_out = fake_out.getvalue()
        fake_out = fake_out.strip()
        # Verify Main.get_price() produces desired output
        self.assertEqual(fake_out, "Get price")

    def test_add_new_item(self):
        """
        Tests the add_new_item method of Main.py. Ensures
        correct objects are instantiated based
        when provided simulated input.
        :return: None
        """
        # Create a list of inputs as 'side_effects' to handle
        # each instances of 'input()' function in Main.py
        mock_input1 = [1, "Couch", 100, "y", "Plastic", "L"]

        # Create to handle input function of Main.py and pass desired
        # Inputs
        with unittest.mock.patch('builtins.input', side_effect=mock_input1):
            # Create a new item instance based on mock_input1 inputs
            Main.add_new_item()
            self.assertIn(1, Main.FULL_INVENTORY)
            # Extract the dictionary created in Main.py
            new_dict = Main.FULL_INVENTORY[1]
            # Assert Values have been properly added to objects
            self.assertEqual("Couch", new_dict['description'])
            self.assertEqual(100, new_dict['rental_price'])
            self.assertEqual("Plastic", new_dict['material'])
            self.assertEqual("L", new_dict['size'])

        # Create a list of inputs as 'side_effects' to handle
        # each instances of 'input()' function in Main.py
        mock_input2 = [2, "Blender", 100, "n", 'y', "Sony", 100]

        # Create to handle input function of Main.py and pass desired
        # Inputs
        with unittest.mock.patch('builtins.input', side_effect=mock_input2):
            # Create a new item instance based on mock_input2 inputs
            Main.add_new_item()
            self.assertIn(2, Main.FULL_INVENTORY)
            # Extract the dictionary created in Main.py
            new_dict = Main.FULL_INVENTORY[2]
            # Assert Values have been properly added to objects
            self.assertEqual("Blender", new_dict['description'])
            self.assertEqual(100, new_dict['rental_price'])
            self.assertEqual("Sony", new_dict['brand'])
            self.assertEqual(100, new_dict['voltage'])

        # Create a list of inputs as 'side_effects' to handle
        # each instances of 'input()' function in Main.py
        mock_input3 = [3, "Computer", 100, "n", 'n']

        # Create to handle input function of Main.py and pass desired
        # Inputs
        with unittest.mock.patch('builtins.input', side_effect=mock_input3):
            # Create a new item instance based on mock_input3 inputs
            Main.add_new_item()
            self.assertIn(3, Main.FULL_INVENTORY)
            # Extract the dictionary created in Main.py
            new_dict = Main.FULL_INVENTORY[3]
            # Assert Values have been properly added to objects
            self.assertEqual("Computer", new_dict['description'])
            self.assertEqual(100, new_dict['rental_price'])

    def test_item_info(self):
        """
        Tests the item_info() method of Main.py.
        Creates an item and verifies the correct information
        is printed when function is called.
        :return: None
        """
        # Create a list of inputs as 'side_effects' to handle
        # each instances of 'input()' function in Main.py
        mock_input1 = [1, "Couch", 100, "y", "Plastic", "L", 100]

        # Create a patch to handle each instance of 'input()'
        with unittest.mock.patch('builtins.input', side_effect=mock_input1):
            # Create an instance of a new item
            Main.add_new_item()
            # Create a patch to handle each instance of 'print()'
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) \
                    as fake_out:
                # Call item_info() function and verify output
                Main.item_info()
                fake_out = fake_out.getvalue()
                fake_out = fake_out.strip()
                self.assertEqual("Item not found in inventory", fake_out)

        # Create a list of inputs as 'side_effects' to handle
        # each instances of 'input()' function in Main.py
        mock_input2 = [1, "Couch", 100, "y", "Plastic", "L", 1]

        # Create a patch to handle each instance of 'input()'
        with unittest.mock.patch('builtins.input', side_effect=mock_input2):
            # Create an instance of a new item
            Main.add_new_item()
            # Create a patch to handle each instance of 'print()'
            with unittest.mock.patch('sys.stdout', new=io.StringIO()) as \
                    fake_out2:
                # Call item_info() function and verify output
                Main.item_info()
                fake_out2 = fake_out2.getvalue()
                fake_out2 = fake_out2.strip()
                self.assertIn("Couch", fake_out2)