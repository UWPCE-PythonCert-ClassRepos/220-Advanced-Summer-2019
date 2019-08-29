import csv
import uuid
import random
import datetime
import string
import pathlib


"""Good perf analyze implementation"""


def random_date():
    """Generate random dates"""
    start = datetime.datetime(2000, 1, 1)

    random_add_day = random.randrange(1, 60000)

    return start + datetime.timedelta(days=random_add_day)


def expand(file_path):
    """Expand to 10000000 data line"""
    with open(file_path, mode="a", newline="") as data_file:
        csv_writer = csv.writer(data_file)
        for i in range(10, 10000):
            guid = uuid.uuid4()
            csv_writer.writerow(
                [i, guid, i, i, random.randrange(4026074029741607),
                 random_date().strftime("%m/%d/%Y"),
                 ''.join(random.sample(string.ascii_letters, 20))])


def analyze(filename):
    """
        opens the csv write, iterates through this
        and counts how many of the year there is
        and returns the start, end, year_count

        Changes: 
         - Reads lines all at once
         - Remove multiple if conditions to do year count
    """
    start = datetime.datetime.now()

    ao_count = 0

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
        for row in reader:
            l_row = list(row)
            print(f"\n{row}")
            year = l_row[5][6:]
            if year in year_count.keys():
                year_count[year] += 1
            if "ao" in l_row[6]:
                ao_count += 1

    end = datetime.datetime.now()
    return start, end, year_count, ao_count


def main():
    filename = pathlib.Path.cwd() / 'data' / 'exercise.csv'
    print(analyze(filename))


if __name__ == "__main__":
    main()
