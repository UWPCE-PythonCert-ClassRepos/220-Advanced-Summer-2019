"""
grade lesson 5
"""

import os
import pytest

import database as db


@pytest.fixture
def _show_available_products():
    # return {
    #     'P000001': {'description': 'Chair Red leather', 'product_type': 'livingroom',
    #                 'quantity_available': '21'},
    #     'P000002': {'description': 'Table Oak', 'product_type': 'livingroom',
    #                 'quantity_available': '4'},
    #     'P000003': {'description': 'Couch Green cloth', 'product_type': 'livingroom',
    #                 'quantity_available': '10'},
    #     'P000004': {'description': 'Dining table Plastic', 'product_type': 'Kitchen',
    #                 'quantity_available': '23'},
    #     'P000005': {'description': 'Stool Black ash', 'product_type': 'Kitchen',
    #                 'quantity_available': '12'}
    #     }

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
    # return {
    #     'C000001': {'name': 'Shea Boehm', 'address': '3343 Sallie Gateway',
    #                 'phone_number': '508.104.0644', 'email': 'Alexander.Weber@monroe.com'},
    #     'C000003': {'name': 'Elfrieda Skiles', 'address': '3180 Mose Row',
    #                 'phone_number': '839)825-0058', 'email': 'Mylene_Smitham@hannah.co.uk'}
    #     }

    return {
        'user008': {'name': 'Shirlene Harris', 'address': '4329 Honeysuckle Lane', 'phone_number': '206-279-5340',
                    'email': 'harrisfamily@gmail.com'},
        'user005': {'name': 'Dan Sounders', 'address': '861 Honeysuckle Lane', 'phone_number': '206-279-1723',
                    'email': 'soundersoccer@mls.com'}
    }


def test_import_data():
    """ import """
    data_dir = 'data'
    added, errors = db.import_data(data_dir, "products.csv", "customers.csv", "rentals.csv")

    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)
    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)


def test_show_available_products(_show_available_products):
    """ available products """
    students_response = db.show_available_products()
    assert students_response == _show_available_products


def test_show_rentals(_show_rentals):
    """ rentals """
    students_response = db.show_rentals("prd002")
    assert students_response == _show_rentals
