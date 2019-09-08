
def print_log(func):
    def logged(*args, **kwargs):
        print(f"Function {func.__name__} called")
        if args:
            print(f"    with args: {args}")
        if kwargs:
            print(f"    with kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"    Result: {result}")
        return result
    return logged

@print_log
def test_logger(a, b="", c=100):
    print(b)
    return a + c

test_logger(123, "testing")