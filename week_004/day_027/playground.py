# Arguments
def add(*numbers):
    print(sum(numbers))


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Keyword Arguments
def greet(**names):
    print(' '.join(names.values()))


greet(first_name="Oscar", last_name="Cruz")
