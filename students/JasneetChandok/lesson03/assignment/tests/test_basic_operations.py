from customer_data.basic_operations import *
# import pytest - Run file using pytest


database = SqliteDatabase("customers_test.db")
database.connect()
database.execute_sql("PRAGMA foreign_keys=ON;")
database.execute_sql('drop table if exists Customer;')
Customer.create_table()


def test_add_customer():
    add_customer(customer_id=1,
                 name="Jasneet",
                 lastname="Chandok",
                 home_address="10688 Fake Street, Seattle, WA",
                 phone_number="321-134-5678",
                 email='jkc.2012@fake.com',
                 status="Active",
                 credit_limit=10000)
    add_customer(customer_id=2,
                 name="Sim",
                 lastname="Kaur",
                 home_address="1234 Fake Street, Everett, WA",
                 phone_number="123-132-4444",
                 email='sim.k@fake.com',
                 status="Active",
                 credit_limit=20000)
    query = Customer.get(Customer.id == 1)
    assert query.name == "Jasneet"
    assert query.lastname == "Chandok"
    assert query.home_address == "10688 Fake Street, Seattle, WA"
    assert query.email == 'jkc.2012@fake.com'


def test_search_customer():
    query = search_customer(customer_id=1)
    assert query['name'] == "Jasneet"
    assert query['lastname'] == "Chandok"
    assert query['phone_number'] == "321-134-5678"
    assert query['email'] == 'jkc.2012@fake.com'


def test_search_customer_invalid_id():
    assert search_customer(customer_id=99) == {}


def test_delete_customer():
    query = Customer.get(Customer.id == 1)
    assert query.name == "Jasneet"

