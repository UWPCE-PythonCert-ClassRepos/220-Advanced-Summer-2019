import csv

data = [
    ['LR01','Small lamp','7.50'],
    ['LR02','Television','28.00'],
    ['BR07','LED lamp','5.50'],
    ['KT08','Basic refrigerator','40.00'],
]

def create_csv_writer(invoice_file):
    def add_transaction(customer, item_code, item_description, item_quantity):
        with open(invoice_file, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([customer, item_code, item_description, item_quantity])
    return add_transaction


transactor = create_csv_writer('demo.csv')

for d in data:
    transactor(*d)


def single_customer(customer_name, invoice_file):
    def add_rental_items(item_code, item_description, item_quantity):
        writer = create_csv_writer(invoice_file)
        writer(customer_name, item_code, item_description, item_quantity)
    return add_rental_items


transactor = single_customer('Elisa Miles', 'elisa.csv')

for d in data:
    transactor(*d[1:])
