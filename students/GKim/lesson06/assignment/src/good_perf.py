"""Program to generate random rows of data for lesson06 assignment"""
import uuid
import csv
import logging
from datetime import date, timedelta
from random import randint, choice, random
# pylint: disable=C0103

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def rdate():
    """Generates random date between 2010-2018"""
    start_date = date(2010, 1, 1)
    years = 9
    end_date = timedelta(years*365)
    random_date = (start_date + end_date * random()).strftime('%m/%d/%Y')
    return random_date

def write_file():
    """Generates a file called "exercise.csv" that contains
    random dates, numbers and letters"""
    with open('exercise.csv', 'w') as filename:
        logger.info('starting to write file')
        for i in range(1000000): # adjust for a million
            l = []
            l.append(i)
            l.append(uuid.uuid4())
            l.append(i)
            l.append(i)
            l.append(randint(10000000000, 10000000000000000))
            l.append(rdate())
            l.append(choice(['ao', None]))
            writer = csv.writer(filename, lineterminator='\n')
            writer.writerow(l)
        logger.info('finished writing file')

if __name__ == '__main__':
    write_file()