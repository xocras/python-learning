# Loops

fruits = ["Apple", "Banana", "Orange", "Grapes", "Strawberry"]

for i, fruit in enumerate(fruits):
    print(f"{i + 1}: {fruit}")

# Range doesn't include the second argument

print("Let's count!")

for n in range(0, 10):
    print(f"{n + 1}...")

print("Done!")

# You can specify the incremental amount when using the range() function.

print("Even numbers!")

for n in range(0, 10, 2):
    print(f"{n + 2}...")

print("Done!")
