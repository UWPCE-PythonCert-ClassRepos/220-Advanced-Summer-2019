"""
grade lesson 5
"""

import os
import pytest

import database as l

@pytest.fixture
def _show_available_products():
    return {'prd001':
            {'description': '60-inch TV stand',
             'product_type': 'livingroom',
             'quantity_available': 'livingroom'},
            'prd003':
            {'description': 'Acacia kitchen table',
             'product_type': 'kitchen',
             'quantity_available': 'kitchen'},
            'prd004':
            {'description': 'Queen bed',
             'product_type': 'bedroom',
             'quantity_available': 'bedroom'},
            'prd005':
            {'description': 'Reading lamp',
             'product_type': 'bedroom',
             'quantity_available': 'bedroom'},
            'prd006':
            {'description': 'Portable heater',
             'product_type': 'bathroom',
             'quantity_available': 'bathroom'},
            'prd008':
            {'description': 'Smart microwave',
             'product_type': 'kitchen',
             'quantity_available': 'kitchen'},
            'prd010':
            {'description': '60-inch TV',
             'product_type': 'livingroom',
             'quantity_available': 'livingroom'}}


@pytest.fixture
def _show_rentals():
    return {'user001':
            {'address': '4490 Union Street',
             'email': 'elisa.miles@yahoo.com',
             'name': 'Elisa Miles',
             'phone_number': '206-922-0882'},
            'user003':
            {'address': '348 Terra Street',
             'email': 'andy.norris@gmail.com',
             'name': 'Andy Norris',
             'phone_number': '206-309-2533'}}


def test_import_data():
    """ import """
    data_dir = "../data"
    added, errors = l.import_data(data_dir, "products.csv", "customers.csv", "rentals.csv")

    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)

    assert added == (10, 9, 10)
    assert errors == (0, 0, 0)

def test_show_available_products(_show_available_products):
    """ available products """
    students_response = l.show_available_products()
    assert students_response == _show_available_products

def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = l.show_rentals("prd005")
    assert students_response == _show_rentals
