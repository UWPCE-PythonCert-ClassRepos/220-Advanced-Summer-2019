"""File generates fake records"""
import random
import string
import csv


def generate_alphanum(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_guid():
    return "-".join([generate_alphanum(8),
                     generate_alphanum(4),
                     generate_alphanum(4),
                     generate_alphanum(4),
                     generate_alphanum(12)])


def generate_num(size, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_ccnumber(size=16):
    return generate_num(size)


def generate_text(size, chars=string.ascii_lowercase + " "):
    return "".join(random.choice(chars) for _ in range(size))


def generate_date():
    month = str(random.choice(range(12)) + 1)
    days = str(random.choice(range(28)) + 1)
    year = str(random.choice(range(1900, 2050)))
    return "/".join([month, days, year])


def generate_rows(number=1000):
    for seq in range(1, number + 1):
        yield [
            seq,
            generate_guid(),
            seq,
            seq,
            generate_ccnumber(),
            generate_date(),
            generate_text(random.randint(10, 24))
        ]


def generate_data_file(filepath, nrows):
    """
    opens csv with filepath and writes nrows fields by calling the generate_row method
    """
    with open(filepath, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        header = ["seq", "guid", "seq", "seq", "ccnumber", "date", "sentence"]
        writer.writerow(header)
        for row in generate_rows(nrows):
            writer.writerow(row)


if __name__ == "__main__":
    """generate 1  million records"""
    generate_data_file("exercise.csv", 10**6)