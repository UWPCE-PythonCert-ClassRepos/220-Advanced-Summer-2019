import csv

data = [
    ["Elisa Miles", "LR04", "Leather Sofa", "25.00"],
    ["Edward Data", "K278", "Leather Sofa", "30.00"],
    ["Alex Gonzales", "LR20", "Automan", "17.00"],
    ["Susan Wong", "LR19", "Microfiber Bed", "17.00"]
]

def add_furniture(invoice_file,
                  customer_name,
                  item_code,
                  item_description,
                  item_monthly_price):
    with open(invoice_file, mode="w+", newline="") as invoice:
        writer = csv.writer(invoice)
        writer.writerow([customer_name,
                        item_code,
                        item_description,
                        item_monthly_price])


def single_customer(customer_name, invoice_file):
    def get_items(rental_items):
        with open(invoice_file, mode="w+", newline="") as invoice:
            writer = csv.writer(invoice)

            with open(rental_items, mode="r") as items:
                reader = csv.reader(items)
                for line in reader:
                    line.insert(0, customer_name)
                    print(line)
                    writer.writerow(line)

    return get_items
