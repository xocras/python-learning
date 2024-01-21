is_new = True
is_on = True

result = 0


def calculate(a, b, operation):
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        return a / b


while is_on:
    a_input = float(input("What's the first number?: ")) if is_new else result

    operation_input = input("\n+\n-\n*\n/\n\nPick an operation: ")

    b_input = float(input("\nWhat's the next number?: "))

    result = calculate(a_input, b_input, operation_input)

    print(f"\n{a_input} {operation_input} {b_input} = {result}")

    next_calculation = input(f"\nType Y to continue with {result}, N to start a new calculation, or E to exit: ")

    is_new = False if next_calculation.upper()[0] == 'Y' else True
    is_on = False if next_calculation.upper()[0] == 'E' else True
