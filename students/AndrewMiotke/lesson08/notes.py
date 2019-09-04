# Closures
def A():
    def B():
        return 5
    return B

a = A()
# returns a functions

# call a and returns 5

b = B()
# returns a NameError

count = 10

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()

"""
Currying
Break down multiple parameters so that you can have a
single or close to a single parameter per function.
"""
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

m10 = make_multiplier(10)
m10(5) # calling m10 returns 50
