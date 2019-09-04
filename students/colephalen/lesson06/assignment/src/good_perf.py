"""
make a nicely written well performing csv reader

"""

import csv
import datetime


def date_pull(list_in):
    """
    grabs the year from huge csv file
    :returns only the year from the date info
    should only return the years we want
    """
    the_list = list_in[5].split('/')[2]
    return the_list


def analyze(filename):
    start = datetime.datetime.now()

    year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0}

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        found = 0

        for row in reader:
            lrow = list(row)
            if lrow[5] > '00/00/2012':
                if lrow[5][6:] == '2013':
                    year_count["2013"] += 1
                if lrow[5][6:] == '2014':
                    year_count["2014"] += 1
                if lrow[5][6:] == '2015':
                    year_count["2015"] += 1
                if lrow[5][6:] == '2016':
                    year_count["2016"] += 1
                if lrow[5][6:] == '2017':
                    year_count["2017"] += 1
                if lrow[5][6:] == '2018':
                    year_count["2018"] += 1

            if "ao" in row[6]:
                found += 1

    end = datetime.datetime.now()

    print(f"'ao' was found {found} times")
    return start, end, year_count, found


def main():
    filename = "/Users/colephalen/220-Advanced-Summer-2019/students/colephalen/lesson06/assignment/src/big_ass_csv.csv"
    # filename = "/Users/colephalen/220-Advanced-Summer-2019/students/colephalen/lesson06/assignment/data/exercise.csv"

    print(analyze(filename))  # added a print statement to see the datetimes


if __name__ == "__main__":
    main()
