import csv
import hashlib

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
            # sentence
            fake.text(),
        ]


def generate_data_file(filepath, nrows):
    """
    """
    with open(filepath, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['seq', 'guid', 'seq', 'seq', 'ccnumber', 'date', 'sentence'])
        for row in generate_rows(nrows):
            writer.writerow(row)


def main():
    filename = "data/test.csv"
    generate_data_file(filename, 1000000)


if __name__ == "__main__":
    main()
