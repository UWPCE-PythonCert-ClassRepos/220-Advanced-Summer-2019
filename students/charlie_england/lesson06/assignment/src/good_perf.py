"""
Okay performing module.
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
    """
    uses the faker module to generate n number of fake people and returns an iterable
    """
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
    """
    opens csv with filepath and writes nrows fields by calling the generate_row method
    """
    with open(filepath, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for row in generate_rows(nrows):
            writer.writerow(row)



def analyze(filename, search_term):
    """
        opens the csv write, iterates through this and counts how many of the year 2013-2018 there is,
        also checks the search_term given as an argument to see how many times this appears
        prints the year_count dictionary and search_term
        returns the start, end, year_count, and found(search_terms found)
    """
    start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        new_ones = []
        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }
        found = 0
        for row in reader:
            if row:
                lrow = list(row)
                if lrow[5] > '00/00/2012':
                    if search_term in row[6]:
                            found +=1
                    try:
                        year_count[lrow[5][-4:]] += 1  
                    except:
                        pass
        print(year_count)
        print(f"'{search_term}' was found {found} times")
        end = datetime.datetime.now()
    return (start, end, year_count, found)


def setup():
    """
    sets up the argument_parser as well as generates data if needed (comment line out for no generation of data)
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--rows", type=int, default=10, help="Number of rows to generate in demo file")
        parser.add_argument("--filename", type=str, default="..//data//demo.csv", help="Filename of demo data")
        parser.add_argument("--search_term", type=str, default="Street", help="Search term to look for in address info")
        args = parser.parse_args()
        # generate_data_file(args.filename, args.rows)
        return args
    except Exception as e:
        print(e)
        exit(-1)

if __name__ == "__main__":
    # SETUP
    args = setup()

    # MAIN
    analyze(args.filename, args.search_term)
    