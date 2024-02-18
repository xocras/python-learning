inputs = [1, 2, 3]


def logging_decorator(f):
    def log(*numbers):
        print(f'You called {f.__name__}({numbers[0]}, {numbers[1]}, {numbers[2]})')
        print(f'It returned: {f(numbers[0], numbers[1], numbers[2])}')
        pass
    return log


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
