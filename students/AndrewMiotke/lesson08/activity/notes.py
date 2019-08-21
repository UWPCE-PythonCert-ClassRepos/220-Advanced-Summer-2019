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
