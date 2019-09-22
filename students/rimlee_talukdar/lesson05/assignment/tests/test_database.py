"""
grade lesson 5
"""

import os
import pytest

import database as l


@pytest.fixture
def _show_available_products():
    return {
        'prd001': {'description': '60-inch TV stand', 'product_type': 'livingroom', 'quantity_available': '3'},
        'prd003': {'description': 'Acacia kitchen table', 'product_type': 'kitchen', 'quantity_available': '7'},
        'prd004': {'description': 'Queen bed', 'product_type': 'bedroom', 'quantity_available': '10'},
        'prd005': {'description': 'Reading lamp', 'product_type': 'bedroom', 'quantity_available': '20'},
        'prd006': {'description': 'Portable heater', 'product_type': 'bathroom', 'quantity_available': '14'},
        'prd008': {'description': 'Smart microwave', 'product_type': 'kitchen', 'quantity_available': '30'},
        'prd010': {'description': '60-inch TV', 'product_type': 'livingroom', 'quantity_available': '3'}
    }

@pytest.fixture
def _show_rentals():
    return {
        'user001': {
            'name': 'Elisa Miles',
            'address': '4490 Union Street',
            'phone_number': '206-922-0882',
            'email': 'elisa.miles@yahoo.com'
        },
        'user003': {
            'name': 'Andy Norris',
            'address': '348 Terra Street',
            'phone_number': '206-309-2533',
            'email': 'andy.norris@gmail.com'
        }
    }



def test_import_data():
    """ import """
    data_dir = os.path.dirname(os.getcwd() + '/data/')
    added, errors = l.import_data(data_dir, "products.csv", "customers.csv", "rentals.csv")

    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)


def test_show_available_products(_show_available_products):
    """ available products """
    available_products_response = l.show_available_products()
    print(available_products_response)
    assert available_products_response == _show_available_products

def test_show_rentals(_show_rentals):
    """ rentals """
    rentals_response = l.show_rentals("prd005")
    print(rentals_response)
    assert rentals_response == _show_rentals
