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
    # return the_list
    if the_list in ['2013', '2014', '2015', '2016', '2017', '2018']:
        return the_list


# unused:
def date_spec(list_in):
    """
    narrows down the dates to only 2013-2018
    :return: list of all the 2013's-2018's
    """


# unused:
def _generate(list_in):
    """
    i want to have this be a quick way to count how often years 2013, 2014, 2015, 2016, 2017 and 2018 occur
    """
    for j in list_in:
        yield date_pull(list_in)


def analyze(filename):
    start = datetime.datetime.now()

    with open(filename, 'r') as the_csv:
        reader = iter(csv.reader(the_csv))
        # added = []  # might not need this anymore to make a list. maping helps speed things up

        next(reader)  # skips the header

        # mapping using the function defined above to pull the year out of the yuge list
        map_iterator = map(date_pull, reader)



        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0}

        for new in map_iterator:
            if new == '2013':
                year_count["2013"] += 1
            if new == '2014':
                year_count["2014"] += 1
            if new == '2015':
                year_count["2015"] += 1
            if new == '2016':
                year_count["2016"] += 1
            if new == '2017':
                year_count["2017"] += 1
            if new == '2018':
                year_count["2018"] += 1

        # # make a list out of the map_iterator !!!works!!!
        # added = list(map_iterator)

        # #  make a set out of the map_iterator !!!works!!!
        # added = set(map_iterator)

        # for row in reader:
        #     added.append(row[5].split('/')[2])

    found = 1

    end = datetime.datetime.now()
    return start, end, year_count, found


def main():
    # filename = "/Users/colephalen/220-Advanced-Summer-2019/students/colephalen/lesson06/assignment/data/exercise.csv"

    filename = "/Users/colephalen/220-Advanced-Summer-2019/students/colephalen/lesson06/assignment/src/big_ass_csv.csv"

    print(analyze(filename))


if __name__ == "__main__":
    main()

