import csv
import uuid
import random
import datetime
import string


"""Good perf analyze implementation"""


def random_date():
    """Generate random dates"""
    start = datetime.datetime(2000, 1, 1)

    random_add_day = random.randrange(1, 60000)

    return start + datetime.timedelta(days=random_add_day)


def expand(file_path):
    """Expand to 10000 data line"""
    with open(file_path, mode="a", newline="") as data_file:
        csv_writer = csv.writer(data_file)
        for i in range(10, 10000):
            guid = uuid.uuid4()
            csv_writer.writerow(
                [i, guid, i, i, random.randrange(4026074029741607),
                 random_date().strftime("%m/%d/%Y"),
                 ''.join(random.sample(string.ascii_letters, 20))])


# expand("data\\exercise.csv")


def analyze(filename):
    """Good performance analyze implementation, read lines once"""
    start = datetime.datetime.now()
    year_count = {
        "2013": 0,
        "2014": 0,
        "2015": 0,
        "2016": 0,
        "2017": 0,
        "2018": 0
    }

    ao_count = 0

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            l_row = list(row)
            print(f"********{row}")
            year = l_row[5][6:]
            if year in year_count.keys():
                year_count[year] += 1
            if "ao" in l_row[6]:
                ao_count += 1

    end = datetime.datetime.now()
    return start, end, year_count, ao_count


def main():
    """Entry point"""
    filename = "../data/exercise.csv"
    print(analyze(filename))


if __name__ == "__main__":
    main()
