"""
import exercise.csv and make it into 1 million lines (9 right now)
"""

import csv
import uuid
import random
import string


def random_str(string_length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(string_length))


def blowing_up(count=5):
    i = 0
    data = ['seq', 'guid', 'seq', 'seq', 'ccnumber', 'date', 'sentence']
    yield data

    while i < count:
        contents = [
            str(i),
            str(uuid.uuid4()),
            str(i),
            str(i),
            str(random.randint(9999999, 99999999)),
            '{}/{}/{}'.format(
                str(random.randint(1, 12)),
                str(random.randint(1, 31)),
                str(random.randint(1900, 2500))),
            random_str(random.randint(1, 50))
        ]
        yield contents
        i += 1


blow = blowing_up(1000000)

with open('big_ass_csv.csv', 'w') as h:
    for j in blow:
        wrte = csv.writer(h)
        wrte.writerow(j)

