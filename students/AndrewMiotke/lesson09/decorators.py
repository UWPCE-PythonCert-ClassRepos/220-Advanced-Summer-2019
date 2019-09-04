# Decoratorates fucntions and wraps more functionality around a function
# Decorators are like closures under the hood


def upper(func):
    """ Creates a decorator """
    def wrapper(*args):
        args = [str(a).upper() for a in args]
        return func(*args)
    return wrapper


@upper # calls the upper function as a decorator
def just_print_it(*strings):
    print(*strings)

words = ["hello", "there", "class"]

just_print_it(words)
