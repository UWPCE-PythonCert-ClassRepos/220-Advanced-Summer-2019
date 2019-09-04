"""
    Autograde Lesson 3 assignment
    Run pytest
    Run coverage and linting using standard batch file
    Student should submit an empty database

"""
import unittest
from test_unit import *
import pytest
import peewee
import logging
import basic_operations as l
import create_customer import customer




# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler('norton.log')
# fh.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s\t%(message)s')
# fh.setFormatter(formatter)
# logger.addHandler(fh)

# or use this
logging.basicConfig(level=logging.DEBUG, filename="customers.db")
LOGGER = logging.getLogger(__name__)


@pytest.fixture
def test_add_customers():
    return customer(
        [
        ("105", "Brenda", "Steinberg", "6042435544", "bs@gmail.com", "active", 850),
        ("456", "Robert", "Green", "6163920404", "rg@gmail.com", "inactive", 650),
        ("190", "Carlos", "Alexander", "2135356643", "ca@gmail.com", "active", 700),
        ("404", "James", "Sinclair", "3135250000", "js@gmail.com", "active", 690),
        ("155", "Tim", "Burton", "5204550030", "tb@gmail.com", "active", 300),
        ("0123", "Riley", "Curry", "5555555555", "rc@gmail.com", "inactive", 340),
        ("777", "Eastley", "Tatum", "4105667943", "et@gmail.com", "active", 500)
        ]
    )



@pytest.fixture
def test_search_customers(): # needs to del with database
    return iter (
        [
        ("105", "Brenda", "Steinberg", "6042435544", "bs@gmail.com", "active", 850),
        ("456", "Robert", "Green", "6163920404", "rg@gmail.com", "inactive", 650),
        ("190", "Carlos", "Alexander", "2135356643", "ca@gmail.com", "active", 700)
        ]
    )

@pytest.fixture
def test_delete_customers(): # needs to del with database
    return iter (
        [
        ("0123", "Riley", "Curry", "5555555555", "rc@gmail.com", "inactive", 340),
        ("777", "Eastley", "Tatum", "4105667943", "et@gmail.com", "active", 500)
        ]
    )

@pytest.fixture
def test_update_customer_credit(): # needs to del with database
    return (
        row for row in [
        ("190", "Carlos", "Alexander", "2135356643", "ca@gmail.com", "active", 700),
        ("404", "James", "Sinclair", "3135250000", "js@gmail.com", "active", 690),
        ("155", "Tim", "Burton", "5204550030", "tb@gmail.com", "active", 300)
        ]
    )

@pytest.fixture
def test_list_active_customers():
    return (
        row for row in [
        ("105", "Brenda", "Steinberg", "6042435544", "bs@gmail.com", "active", 850),
        ("456", "Robert", "Green", "6163920404", "rg@gmail.com", "inactive", 650),
        ("190", "Carlos", "Alexander", "2135356643", "ca@gmail.com", "active", 700),
        ("404", "James", "Sinclair", "3135250000", "js@gmail.com", "active", 690),
        ("155", "Tim", "Burton", "5204550030", "tb@gmail.com", "active", 300),
        ("0123", "Riley", "Curry", "5555555555", "rc@gmail.com", "inactive", 340),
        ("777", "Eastley", "Tatum", "4105667943", "et@gmail.com", "active", 500)
        ]
    )

def test_list_active_customers(list_active_customers):
    """ actives """
    for customer in list_active_customers:
        add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
    actives = list_active_customers()

    assert actives == 2

    for customer in list_active_customers:
        delete_customer(customer[0])



def test_add_customer(add_customers):
    """ additions """
    for customer in add_customers:
        add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
        added = search_customer(customer[0])
        assert added["name"] == customer[1]
        assert added["lastname"] == customer[2]
        assert added["email"] == customer[5]
        assert added["phone_number"] == customer[4]

    for customer in _add_customers:
        self.delete_customer(customer[0])



def test_search_customer(search_customers[0]):
    """ search """
    for customer in _search_customers[0]:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

    result = l.search_customer(_search_customers[1][1])
    assert result == {}

    result = l.search_customer(_search_customers[1][0])
    assert result["name"] == _search_customers[0][1][1]
    assert result["lastname"] == _search_customers[0][1][2]
    assert result["email"] == _search_customers[0][1][5]
    assert result["phone_number"] == _search_customers[0][1][4]

    for customer in _search_customers[0]:
        l.delete_customer(customer[0])


def test_delete_customer(_delete_customers):
    """ delete """
    for customer in _delete_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

        response = delete_customer(customer[0])
        assert response is True

        deleted = search_customer(customer[0])
        assert deleted == {}

def test_update_customer_credit(_update_customer_credit):
    """ update """
    for customer in _update_customer_credit:
        add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )

    l.update_customer_credit("798", 0)
    l.update_customer_credit("797", 1000)
    l.update_customer_credit("797", -42)
    l.update_customer_credit("796", 500)
    with pytest.raises(ValueError) as excinfo:
        l.update_customer_credit("00100", 1000) # error
        assert 'NoCustomer'  in str(excinfo.value)
