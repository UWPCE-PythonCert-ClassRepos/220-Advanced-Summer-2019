"""
Better performing module
"""

import datetime
import csv


def analyze(filename):
    start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
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
            list_row = list(row)
            year = list_row[5][6:]
            text = list_row[6]
            if year in year_count.keys():
                year_count[year] += 1
            if "ao" in text:
                found += 1

        print(year_count)
        print(f"'ao' was found {found} times")

        end = datetime.datetime.now()

        return start, end, year_count, found


def main():
    filename = "data/exercise.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
