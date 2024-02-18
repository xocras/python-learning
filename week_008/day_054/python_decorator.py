from time import perf_counter


def speed_calc_decorator(function):
    def print_time():
        start = perf_counter()
        function()
        end = perf_counter()
        print(f'\n{function.__name__} run speed: {end - start} seconds')

    return print_time


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        result = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        result = i * i


fast_function()
slow_function()
