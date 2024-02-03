# Errors
students = ["Oscar", "Wilson", "Nelson"]

try:
    index = int(input("Enter the index for your chosen student: "))

    if index == 777:
        raise SystemError("You found the hidden bug!")

    print(students[index])

except ValueError:
    print("That's not a number!")
except IndexError:
    print("That student doesn't exist!")
else:
    print("That's your student!")
finally:
    print("Goodbye!")
