'''
    Autograde Lesson 8 assignment

'''

import csv
import pytest

import inventory as l


@pytest.fixture
def _show_all_furniture():
    return (
        ['Elisa Miles', 'LR04', 'Leather Sofa', '25'],
        ['Edward Data', 'KT78', 'Kitchen Table', '10'],
        ['Alex Gonzales', 'BR02', 'Queen Mattress', '17']
    )


@pytest.fixture
def _show_all_single_customer_furniture():
    return (
        ['Susan Wong', 'LR04', 'Leather Sofa', '25'],
        ['Susan Wong', 'KT78', 'Kitchen Table', '10'],
        ['Susan Wong', 'BR02', 'Queen Mattress', '17']
    )


def test_add_furniture(_show_all_furniture):
    # Remove any old furniture listing in the spreadsheet’s data
    with open('data/rented_items.csv', mode='w') as invoice:
        invoice.close()

    l.add_furniture('data/rented_items.csv', 'Elisa Miles', 'LR04', 'Leather Sofa', 25)
    l.add_furniture('data/rented_items.csv', 'Edward Data', 'KT78', 'Kitchen Table', 10)
    l.add_furniture('data/rented_items.csv', 'Alex Gonzales', 'BR02', 'Queen Mattress', 17)

    with open('data/rented_items.csv', mode='r') as invoice:
        reader = csv.reader(invoice, delimiter=',')
        for read_furniture, acutal_furniture in zip(reader, _show_all_furniture):
            assert read_furniture == acutal_furniture


def test_single_customer(_show_all_single_customer_furniture):
    # Remove any old furniture listing in the spreadsheet’s data
    with open('data/test_items.csv', mode='w') as invoice:
        invoice.close()

    create_invoice = l.single_customer('Susan Wong', 'data/rented_items.csv')
    create_invoice('data/test_items.csv')

    with open('data/test_items.csv', mode='r') as invoice:
        reader = csv.reader(invoice, delimiter=',')
        for read_furniture, acutal_furniture in zip(reader, _show_all_single_customer_furniture):
            assert read_furniture == acutal_furniture
