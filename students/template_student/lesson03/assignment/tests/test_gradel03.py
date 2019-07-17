"""
    Autograde Lesson 3 assignment
    Run pytest
    Run cobverage and linitng using standard batch file
    Student should submit an empty database

"""

import pytest

import basic_operations as l

@pytest.fixture
def _add_customers():
    return [
        ("123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("456", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("789", "Name", "Lastname", "Address", "phone", "email", "active", 0),
        ("345", "Name", "Lastname", "Address", "phone", "email", "active", -10),
        ("0123", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("777", "Name", "Lastname", "Address", "phone", "email", "active", 999)
    ]

@pytest.fixture
def _search_customers(): # needs to del with database
    return [
        [("998", "Name", "Lastname", "Address", "phone", "email", "active", 999),
         ("997", "Name", "Lastname", "Address", "phone", "email", "inactive", 10)],
        ("998", "000")
    ]
@pytest.fixture
def _delete_customers(): # needs to del with database
    return [
        ("898", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("897", "Name", "Lastname", "Address", "phone", "email", "inactive", 10)
    ]

@pytest.fixture
def _update_customer_credit(): # needs to del with database
    return [
        ("798", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("797", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("796", "Name", "Lastname", "Address", "phone", "email", "inactive", -99)
    ]

@pytest.fixture
def _list_active_customers():
    return [
        ("598", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("597", "Name", "Lastname", "Address", "phone", "email", "inactive", 10),
        ("596", "Name", "Lastname", "Address", "phone", "email", "inactive", 99),
        ("595", "Name", "Lastname", "Address", "phone", "email", "active", 999),
        ("594", "Name", "Lastname", "Address", "phone", "email", "active", 10),
        ("593", "Name", "Lastname", "Address", "phone", "email", "active", 99)
    ]

def test_list_active_customers(_list_active_customers):
    """ actives """
    for customer in _list_active_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
    actives = l.list_active_customers()

    assert actives == 2

    for customer in _list_active_customers:
        l.delete_customer(customer[0])



def test_add_customer(_add_customers):
    """ additions """
    for customer in _add_customers:
        l.add_customer(customer[0],
                       customer[1],
                       customer[2],
                       customer[3],
                       customer[4],
                       customer[5],
                       customer[6],
                       customer[7]
                       )
        added = l.search_customer(customer[0])
        assert added["name"] == customer[1]
        assert added["lastname"] == customer[2]
        assert added["email"] == customer[5]
        assert added["phone_number"] == customer[4]

    for customer in _add_customers:
        l.delete_customer(customer[0])



def test_search_customer(_search_customers[0]):
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

        response = l.delete_customer(customer[0])
        assert response is True

        deleted = l.search_customer(customer[0])
        assert deleted == {}

def test_update_customer_credit(_update_customer_credit):
    """ update """
    for customer in _update_customer_credit:
        l.add_customer(customer[0],
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
