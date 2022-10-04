"add called with 4, 5"

def logger(func):
    def inner(*args):
        print(func.__name__)
    return inner


@logger
def add(x, y):
    return x + y
add(4, 5)

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

square_all(4, 5)