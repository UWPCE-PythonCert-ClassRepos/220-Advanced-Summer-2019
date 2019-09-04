"""
good module

"""

import datetime
import csv


def analyze(filename):
    start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        found = 0
        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }
        for row in reader:
            lrow = list(row)
            if "ao" in row[6]:
                found += 1
            try:
                year_count[lrow[5][-4:]] += 1
            except:
                pass
        print(year_count)

    print(f"'ao' was found {found} times")
    end = datetime.datetime.now()
    print(end - start)
    return (start, end, year_count, found)


def main():
    filename = "../data/exercise.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
