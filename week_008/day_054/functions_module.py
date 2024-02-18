def outer_function():
    print('Called from the outside!')

    def inner_function():
        print('Called from the inside of another function!')

    return inner_function


returned_function = outer_function()

returned_function()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate(operation, a, b):
    print(operation(a, b))


calculate(add, 10, 20)

calculate(multiply, 10, 20)
