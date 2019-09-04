import csv
from functools import partial


def add_furniture(invoice_file, customer_name, item_code,
                  item_description, item_monthly_price):
    with open(invoice_file, 'a+', newline='') as file:
        writer = csv.writer(file)
        row = customer_name, item_code, item_description, item_monthly_price
        writer.writerow(row)


def single_customer(customer_name, invoice_file):
    def add_rentals(rental_items):
        with open(rental_items) as file:
            reader = csv.reader(file)
            add_item = partial(add_furniture,
                               invoice_file=invoice_file,
                               customer_name=customer_name)
            for row in reader:
                """First cut
                add_furniture(invoice_file=invoice_file,
                              customer_name=customer_name,
                              item_code=row[0],
                              item_description=row[1],
                              item_monthly_price=row[2])"""
                add_item(item_code=row[0],
                         item_description=row[1],
                         item_monthly_price=row[2])
    return add_rentals


if __name__ == "__main__":
    add_furniture("../data/rented_items.csv", "Elisa Miles",
                  "LR04", "Leather Sofa", 25)
    add_furniture("../data/rented_items.csv", "Edward Data",
                  "../data/KT78", "Kitchen Table", 10)
    add_furniture("../data/rented_items.csv", "Alex Gonzales",
                  "BR02", "Queen Mattress", 17)
    create_invoice = single_customer("Susan Wong", "../data/rented_items.csv")
    create_invoice("../data/test_items.csv")
