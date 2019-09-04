# Recursion is a function that calls itself.
# Could be a replacement for loops
import time

# Basic recursion
def count_down(start, end=0):
    if start > end:
        print(start)
        count_down(start-1, end) # calls the function count_down()


count_down(10, -10)


# Functional way to do a recursion loop
def some_work(i):
        time.sleep(3)
        print("did some work")


def loop(i, func):
    if i > 0:
        func(i)
        loop(i-1, func)

loop(10, some_work)

