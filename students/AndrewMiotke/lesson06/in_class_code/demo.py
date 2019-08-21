""" In class code """

import math
import time
# from timeit import timeit


def do_math():
    for n in range(1000, 1000000):
        math.sqrt(n)


def take_break():
    time.sleep(2)


def do_work():
    for n in range(1000, 10000):
        [x for x in range(n)]


if __name__ == '__main__':
    # print(timeit('[x for x in range(100)]', number=1000))
    # print(timeit(lambda: [x for x in range(100)], number=1000))
    # print(timeit(do_math, number=1000)
    # print(timeit(do_work, number=1000)

    do_math()
    take_break()
    do_work()
    take_break()
