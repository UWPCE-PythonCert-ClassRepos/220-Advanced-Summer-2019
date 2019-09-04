# Context managers help with things like opening and closing
# files, possibly preserving state
# Provides context to the scope of a function or method


# Example of context manager
# with open("#", "w") as file:
#     pass


class C:
    def __init__(self):
        print("Initializing context manager")
        self.x = 0


    def __enter__(self):
        print("entering context manager")
        self.x = 5
        return self


    def __exit__(self, exit_type, exit_value, exit_traceback):
        print("Exiting context manager")
        self.x = -1

with C() as c:
    print(c.x) # returns 5
