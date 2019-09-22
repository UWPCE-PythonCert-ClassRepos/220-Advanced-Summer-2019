from functools import partial
import csv
import logging

def add_furniture(invoice_file, customer_name, item_code, item_description, item_monthly_price):
    with open(invoice_file, 'a+') as invoice:
        writer = csv.writer(invoice, delimiter=',')
        writer.writerow([customer_name, item_code, item_description, item_monthly_price])


def single_customer(customer_name, invoice_file):
    rfunc = partial(add_furniture, customer_name = customer_name, invoice_file = invoice_file)
    return rfunc

def data_feeder():
    try:
        with open('data/test_items.csv') as test:
            reader = csv.reader(test, delimiter = ',')
            results = []
            for row in reader:
                result = []
                for column in row:
                    result.append(column)
                results.append(result)
            return results
    except Exception as e:
        print(e)


if __name__ == '__main__':
    data = data_feeder()
    new_func = single_customer('Arch Wu', 'data/mummy.csv')
    for dat in data:
        item_code, item_description, item_monthly_price = dat[:]
        add_furniture('data/dummy.csv', 'Someone Else',item_code, item_description, item_monthly_price)
        new_func(item_code=item_code, item_description=item_description, item_monthly_price=item_monthly_price)
    
    
            