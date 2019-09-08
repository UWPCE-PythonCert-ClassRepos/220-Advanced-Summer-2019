import csv


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
        # write invoice for this customer
        with open(invoice_file, mode="w+", newline="") as invoice:
            writer = csv.writer(invoice)

            # read rental items
            with open(rental_items, mode="r") as items:
                reader = csv.reader(items)
                for line in reader:
                    line.insert(0, customer_name)
                    print(line)
                    writer.writerow(line)

    return get_items

    if __name__ == "__main__":
        add_furniture("../data/rented_items.csv", "Jas Kaur",
                      "LR04", "Leather Chair", 25)
        add_furniture("../data/rented_items.csv", "Sanjam Patwalia",
                      "../data/KT78", "Dining Table", 10)
        add_furniture("../data/rented_items.csv", "Sanaj Aneet",
                      "BR02", "Full Mattress", 17)
        create_invoice = single_customer("Susan Wong", "../data/rented_items.csv")
        create_invoice("../data/test_items.csv")
