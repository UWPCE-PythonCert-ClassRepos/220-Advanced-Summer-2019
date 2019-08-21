from unittest import TestCase
from unittest.mock import patch
import pytest
import os

from database import import_data, show_rentals, delete_database
from database import show_customers, show_available_products


class TestDatabase(TestCase):

    """"test for Mongo database.py"""
    folder_name = ""
    cwd = os.getcwd()
    folder_name = os.path.join(os.path.abspath(cwd), "data")

    def test_import_data(self):

        """test import all good data"""
        delete_database()

        test_import = import_data(self.folder_name, 'inventory.csv',
                                  'customers.csv', 'rental.csv')

        self.assertEqual(test_import, ((7, 9, 7), (0, 0, 0)))
        
        """test import bad data"""
        delete_database()
        test_import = import_data(self.folder_name, 'inventory1.csv',
                                  'customers2.csv', 'rental3.csv')

        self.assertEqual(test_import, ((0, 0, 0), (1, 1, 1)))

    def test_show_rentals(self):

        """test for show_rentals"""

        delete_database()

        import_data(self.folder_name, 'inventory.csv',
                    'customers.csv', 'rental.csv')

        rental_list = []

        rental_list = show_rentals('p00001')

        gold = [{'Customer_ID': 'c00001', 'Name': 'Danny Holme',
                 'Home_Address': '231 Richland Street, Santa Ana, CA, 33133',
                 'Phone_Number': '253-111-8988',
                 'Email_Address': 'd.zbornak@gmail.com'},
                {'Customer_ID': 'c00007', 'Name': 'Bettey White',
                 'Home_Address': '232 Mohuland Drive, Hollywood, CA, 98546',
                 'Phone_Number': '555-444-4444',
                 'Email_Address': 'b.white@gmail.com'}]

        for r, g in zip(rental_list, gold):
            self.assertDictEqual(r, g)

        self.assertEqual(len(rental_list), 2)

    def test_show_available_products(self):

        """rest for show_available_products"""

        delete_database()

        import_data(self.folder_name, 'inventory.csv',
                    'customers.csv', 'rental.csv')

        product_dict = show_available_products()

        gold = {'Product_ID': 'p00007', 'Description': 'ipad',
                'Type': 'electronic', 'Total_Quantity': 15}

        self.assertDictEqual(product_dict['p00007'], gold)

    def test_show_customers(self):

        """test for show_customers"""

        delete_database()

        import_data(self.folder_name, 'inventory.csv',
                    'customers.csv', 'rental.csv')

        customers_dict = show_customers()

        gold = {'Customer_ID': 'c00007', 'Name': 'Bettey White',
                 'Home_Address': '232 Mohuland Drive, Hollywood, CA, 98546',
                 'Phone_Number': '555-444-4444',
                 'Email_Address': 'b.white@gmail.com',
                 'Status': 1,
                 'Credit_Limit': 100000}

        self.assertDictEqual(customers_dict['c00007'], gold)

# if __name__ == "__main__":

#     test = TestDatabase()

#     test.test_import_data()

#     test.test_show_rentals()

#     test.test_show_customers()

#     test.test_show_available_products()