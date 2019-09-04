import sys
sys.path.insert(0, '../src')

import unittest
import basic_operations as bo


class BasicOperationsTest(unittest.TestCase):

    def test_add_customer(self):
        bo.add_customer("123", "Name", "Lastname", "Address", "phone", "email", "Active", 999)
        bo.add_customer("1234", "Name", "Lastname", "Address", "phone", "email", "Active", 9998)
        bo.add_customer("12345", "Name", "Lastname", "Address", "phone", "email", "Active", 9997)


    def test_search_customer(self):
        bo.add_customer("777", "Name1", "Lastname2", "Address", "phone4", "email3", "Active", 999)
        expected_customer = {
            'name': "Name1",
            'lastname': "Lastname2",
            'email_address': "email3",
            'phone_number': "phone4",
        }
        found_customer = bo.search_customer("777")
        assert expected_customer == found_customer


    def test_delete_customer(self):
        bo.add_customer("888", "Name5", "Lastname6", "Address", "phone8", "email7", "Active", 999)
        expected_customer = {
            'name': "Name5",
            'lastname': "Lastname6",
            'email_address': "email7",
            'phone_number': "phone8",
        }
        found_customer = bo.search_customer("888")
        assert expected_customer == found_customer
        expected_customer = {}
        bo.delete_customer("888")
        found_customer = bo.search_customer("888")
        assert expected_customer == found_customer


    def test_update_customer_credit(self):
        bo.add_customer("999", "Name5", "Lastname6", "Address", "phone8", "email7", "Active", 50)
        bo.update_customer_credit("999",100)


    def test_list_active_customers(self):
        initial_count = bo.list_active_customers()
        bo.add_customer("456", "Name5", "Lastname6", "Address", "phone8", "email7", "Inactive", 50)
        now_count = bo.list_active_customers()
        assert initial_count == now_count
        bo.add_customer("234", "Name5", "Lastname6", "Address", "phone8", "email7", "Active", 50)
        now_count = bo.list_active_customers()
        assert initial_count+1 == now_count