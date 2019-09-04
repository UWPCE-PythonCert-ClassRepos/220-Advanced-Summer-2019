"""
    Autograde Lesson 8 assignment

"""
import sys
sys.path.insert(1,"..//src")
import pytest
import inventory as l
import csv

#reset demo.csv file
with open('demo.csv','w'):
    pass

def test_add_furniture():
    transactor = l.create_csv_writer('demo.csv')
    data = [
        ['Elisa','Lr04','leather sofa','25.00'],
        ['Alex','KT78','Kitchen table','10.00'],
    ]
    for d in data:
        transactor(*d)
    opt_list = []
    with open('demo.csv', 'r') as file:
        [opt_list.append(line.strip('\r\n').split(',')) for line in file.readlines()]
        for data_line in data:
            assert data_line in opt_list
    
def test_single_customer():
    create_invoice = l.single_customer("Susan Wong", "demo.csv")
    create_invoice("test_items.csv")
    data = [
        ['Susan Wong','LR01','Small lamp','7.50'],
        ['Susan Wong','LR02','Television','28.00'],
        ['Susan Wong','BR07','LED lamp','5.50'],
        ['Susan Wong','KT08','Basic refrigerator','40.00']
    ]
    opt_list = []
    with open('demo.csv', 'r') as file:
        [opt_list.append(line.strip('\r\n').split(',')) for line in file.readlines()]
        for data_line in data:
            assert data_line in opt_list
