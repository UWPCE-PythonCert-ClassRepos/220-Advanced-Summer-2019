from customer_data.basic_operations import *
import pytest


database = SqliteDatabase("customers_test.db")
database.connect()
database.execute_sql("PRAGMA foreign_keys=ON;")
database.execute_sql('drop table if exists Customer;')
Customer.create_table()


def test_add_customer():
    add_customer(customer_id=1,
                 name="Brian",
                 lastname="Ervin",
                 home_address="1234 Fake Street, Seattle, WA",
                 phone_number="123-134-4444",
                 email='brian.ervin@fake.com',
                 status="Active",
                 credit_limit=10000)
    add_customer(customer_id=2,
                 name="Felipe",
                 lastname="Rocha",
                 home_address="1234 Fake Street, Everett, WA",
                 phone_number="123-132-4444",
                 email='felipe.rocha@fake.com',
                 status="Active",
                 credit_limit=20000)
    query =  Customer.get(Customer.id == 1)
    assert query.name == "Brian"
    assert query.lastname == "Ervin"
    assert query.home_address == "1234 Fake Street, Seattle, WA"
    assert query.email == "brian.ervin@fake.com"


def test_search_customer():
    query = search_customer(customer_id=1)
    assert query['name'] == "Brian"
    assert query['lastname'] == "Ervin"
    assert query['phone_number'] == "123-134-4444"
    assert query['email'] == "brian.ervin@fake.com"


def test_search_customer_invalid_id():
    assert search_customer(customer_id=99) == {}


def test_delete_customer():
    query = Customer.get(Customer.id == 1)
    assert query.name == "Brian"
    # delete_customer(customer_id=1)
    # assert Customer.get(Customer.id == 1) == {}
