iterable = [9, 8, 2, 3, 1000]

# Map
def d(x):
    return x + 10

# lambda is a short non-named function
it = map(lambda x: x+10, [9, 8, 2, 3, 1000] # creates an object
#next(it) # adds the next item in a list as the lambda "argument"

# Zip
a = ('gus', 'maggie', 'andrew')
b = ('gus', 'saunders', 'miotke')

x = zip(a, b)
print(x)

# Itertools
import itertools

capital_letters = [chr(x) for x in range(65,91)]
print(capital_letters)

it = itertools.isslice(capital_letters, 10, 20)

# Create your own iterator
m = ['k', 'l', 'w']

it = m.__iter__() # adds iterator to `it`
it.__next__()
