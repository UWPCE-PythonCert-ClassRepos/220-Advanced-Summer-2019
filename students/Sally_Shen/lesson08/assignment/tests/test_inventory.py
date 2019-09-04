"""
    Autograde Lesson 8 assignment

"""
import sys
sys.path.append("../src/")

import inventory

inventory.add_furniture("rented_items.csv", "Elisa Miles", "LR04", "Leather Sofa", 25)
inventory.add_furniture("rented_items.csv", "Edward Data", "KT78", "Kitchen Table", 10)
inventory.add_furniture("rented_items.csv", "Alex Gonzales", "BR02", "Queen Mattress", 17)
create_invoice = inventory.single_customer("Susan Wong", "rented_items.csv")
create_invoice("..\\data\\test_items.csv")