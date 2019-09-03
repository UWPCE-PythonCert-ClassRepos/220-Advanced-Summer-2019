import csv

data = [
    ["Elisa miles", "LR04", "Queen Mattress", "17.00"],
    ["Thom Sam", "LR05", "Kig Mattress", "16.00"],
    ["Richie Bilkins", "LR07", "Single Mattress", "12.00"],
    ["Bart Sampson", "LR12", "Leather Sofa", "19.00"]
]

def create_csv_writer(invoice_file):
    def add_transaction(customer, item_code, item_description, item_quantity):
        with open(invoice_file, "a") as file:
            writer = csv.writer(file)
            writer.writerow([customer, item_code, item_description, item_quantity])
    return add_transaction

transactor = create_csv_writer("demo.csv")

def single_customer(customer_name, invoice_file):
    def add_rental_items(item_code, item_description, item_quantity):
        writer = create_csv_writer(invoice_file)
        writer(customer_name, item_code, item_description, item_quantity)
    return add_rental_items

transactor = single_customer("Elisa miles", "elisa.csv")

for d in data:
    transactor(*d[1:])


def add_furniture(invoice_file, customer_name, item_code, item_description, item_monthly_price):
    with open('invoice_file.csv', 'a') as invoice_file:
        writer = csv.writer(invoice_file)
        writer.writerow([invoice_file, customer_name, item_code,
                         item_description, item_monthly_price])
    return add_furniture # do I really need to return this here??

