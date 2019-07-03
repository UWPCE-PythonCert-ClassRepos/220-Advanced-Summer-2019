import pytest
import os

import database as l

@pytest.fixture
def _show_available_products():
    return {
            'P000001':{'description':'Chair Red leather','product_type':'livingroom','quantity_available':'21'},
            'P000002':{'description':'Table Oak','product_type':'livingroom','quantity_available':'4'},
            'P000003':{'description':'Couch Green cloth','product_type':'livingroom','quantity_available':'10'},
            'P000004':{'description':'Dining table Plastic','product_type':'Kitchen','quantity_available':'23'},
            'P000005':{'description':'Stool Black ash','product_type':'Kitchen','quantity_available':'12'}
           }    

@pytest.fixture
def _show_rentals():
    return {
            'C000001':{'name':'Shea Boehm','address':'3343 Sallie Gateway','phone_number':'508.104.0644','email':'Alexander.Weber@monroe.com'},
            'C000003':{'name':'Elfrieda Skiles','address':'3180 Mose Row','phone_number':'839)825-0058','email':'Mylene_Smitham@hannah.co.uk'}
           }

def test_import_data():
    dir = os.path.dirname(os.path.abspath(__file__))
    added, errors = l.import_data(dir, "products.csv", "customers.csv", "rentals.csv")
    for add in added:
        assert isinstance(add, int)
    for error in errors:
        assert isinstance(error, int)  
    assert added == (5,11,9)
    assert errors == (0,0,0)

def test_show_available_products(_show_available_products):
    students_response = l.show_available_products()
    assert students_response == _show_available_products

def test_show_rentals(_show_rentals):
    students_response = l.show_rentals("P000003")
    assert students_response == _show_rentals
