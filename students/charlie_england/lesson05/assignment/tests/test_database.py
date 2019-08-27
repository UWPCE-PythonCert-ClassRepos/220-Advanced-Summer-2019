"""
grade lesson 5
"""

import os
import sys
import pytest
sys.path.insert(0,'../src')
import database as l

@pytest.fixture
def _show_available_products():
    return {
        'prd001': {'description': '60-inch TV stand', 'product_type': 'livingroom',
                    'quantity_available': '3'},
        'prd003': {'description': 'Acacia kitchen table', 'product_type': 'kitchen',
                    'quantity_available': '7'},
        'prd004': {'description': 'Queen bed', 'product_type': 'bedroom',
                    'quantity_available': '10'},
        'prd005': {'description': 'Reading lamp', 'product_type': 'bedroom',
                    'quantity_available': '20'},
        'prd006': {'description': 'Portable heater', 'product_type': 'bathroom',
                    'quantity_available': '14'},
        'prd008': {'description': 'Smart microwave', 'product_type': 'kitchen',
                    'quantity_available': '30'},
        'prd010': {'description': '60-inch TV', 'product_type': 'livingroom',
                    'quantity_available': '3'}
        }

@pytest.fixture
def _show_rentals():
    return {
        'user008': {'name': 'Shirlene Harris', 'address': '4329 Honeysuckle Lane',
                    'phone_number': '206-279-5340', 'email': 'harrisfamily@gmail.com'},
        'user005': {'name': 'Dan Sounders', 'address': '861 Honeysuckle Lane',
                    'phone_number': '206-279-1723', 'email': 'soundersoccer@mls.com'}
        }

def test_import_data():
    """ import """
    data_dir = os.path.join('..', 'data')
    added, errors = l.import_data(data_dir, "product.csv", "customers.csv", "rental.csv")

    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)

def test_show_available_products(_show_available_products):
    """ available products """
    students_response = l.show_available_products()
    assert students_response == _show_available_products

def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = l.show_rentals("prd002")
    assert students_response == _show_rentals
