# seq, guid, seq, seq, ccnumber, date, sentence

import datetime
import uuid
import csv
from lorem.text import TextLorem
import random

def generate_data(file):
    # opening the csv file to find the amount of lines & seq number
    with open(file, 'r') as infile:
        seq = len(infile.readlines())

    while seq < 1000002:
        # generate guid
        guid = uuid.uuid4()

        # generate fake cc
        cc_len = 16
        ccnumber = ''.join(["%s" % random.randint(0, 9)
                            for num in range(0, cc_len)])

        # generate random date because ???
        date = datetime.date(random.randint(2005, 2025),
                            random.randint(1, 12), random.randint(1, 28)).strftime("%d/%m/%Y")

        # generate sentence filled with gibberish??? okay...
        lorem = TextLorem(wsep=' ', srange=(6, 12))
        sentence = lorem.sentence()

        # now we are writing the data to the csv until we have 1 mil entries
        
        with open(file, 'a') as outfile:
        # seq len is one extra b/c of header, but that works instead of +=
            writer = csv.writer(outfile)
            row = [seq, guid, seq, seq, ccnumber, date, sentence]
            writer.writerow(row)
            seq += 1

def analyze(file):
    # literally not even sure what this is supposed to do
    return 'ao' in file


def main():
    generate_data('exercise.csv')
    analyze('exercise.csv')



if __name__ == "__main__":
    main()
