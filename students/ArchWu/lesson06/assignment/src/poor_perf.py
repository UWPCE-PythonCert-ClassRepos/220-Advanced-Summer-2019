"""
Poorly performing, poorly written module.
Create new 'good_perf.py' file and modify there.

How to run this file from the "assignment" folder:

    python src/poor_perf.py --rows 1000 --filename data/demo.csv --search_term Unit

"""

import datetime
import hashlib
import csv
import argparse



"""
    pip install Faker
"""
from faker import Faker
fake = Faker()

def generate_rows(n):
    for i in range(n):
        yield [
            # seq
            i,
            # guid-like id
            hashlib.sha224(bytes(i)).hexdigest(),
            # seq
            i,
            # seq
            i,
            # cc_number 
            fake.credit_card_number(card_type=None),
            # expire_date
            fake.date_between('-6y', '+0y').strftime("%m/%d/%Y"),
            # billing_address
            fake.address(),
        ]

def generate_data_file(filepath, nrows):
    with open(filepath, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for row in generate_rows(nrows):
            writer.writerow(row)



def analyze(filename, search_term):
    start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        new_ones = []
        for row in reader:
            lrow = list(row)
            if lrow[5] > '00/00/2012':
                new_ones.append((lrow[5], lrow[0]))

        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }

        for new in new_ones:
            if new[0][6:] == '2013':
                year_count["2013"] += 1
            if new[0][6:] == '2014':
                year_count["2014"] += 1
            if new[0][6:] == '2015':
                year_count["2015"] += 1
            if new[0][6:] == '2016':
                year_count["2016"] += 1
            if new[0][6:] == '2017':
                year_count["2017"] += 1
            if new[0][6:] == '2018':
                year_count["2017"] += 1

        print(year_count)

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        found = 0

        for line in reader:
            lrow = list(line)
            if search_term in line[6]:
                found += 1

        print(f"'{search_term}' was found {found} times")
        end = datetime.datetime.now()
        print(end-start)

    return (start, end, year_count, found)


def setup():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--rows", type=int, default=10, help="Number of rows to generate in demo file")
        parser.add_argument("--filename", type=str, default="data/demo.csv", help="Filename of demo data")
        parser.add_argument("--search_term", type=str, default="Street", help="Search term to look for in address info")
        args = parser.parse_args()
        generate_data_file(args.filename, args.rows)
        return args
    except Exception as e:
        print(e)
        exit(-1)

if __name__ == "__main__":
    # SETUP
    args = setup()

    # MAIN
    analyze(args.filename, args.search_term)
