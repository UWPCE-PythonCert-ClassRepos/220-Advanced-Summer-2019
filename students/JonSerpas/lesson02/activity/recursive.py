"""
recursion for debuging
"""

import sys


def my_fun(n):
    if n == 2:
        return True
    return my_fun(n / 2)


if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        print(my_fun(n))
    except Exception as e:
        with open('debug.log', 'r+') as output:
            print(e, '\n')
    except SyntaxError as e:
        with open('debug.log', 'r+') as output:
            print(e, '\n')
