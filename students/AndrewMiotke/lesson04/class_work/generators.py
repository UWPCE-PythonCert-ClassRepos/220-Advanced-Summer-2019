"""
Generators are iterators that returns a value
"""

def y_range(start, stop, step=1):
    """ Create a generator using yield """
    i = start
    while i < stop:
        """
        yield, like next(), allows you to increment your flow control
        e.g. inside a loop
        """
        yield i
        i += step

it = y_range(12, 25)
next(it) # this returns 12
next(it) # this returns 13


# Generators in a list comprehension
[y for y in y_range(12, 25)]

