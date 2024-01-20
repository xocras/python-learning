# FizzBuzz!
for n in range(1, 101):
    message = ''
    if not (n % 3):
        message += 'Fizz'
    if not (n % 5):
        message += 'Buzz'
    print(message) if len(message) else print(n)
