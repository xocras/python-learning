# Leap Year
year = int(input("Enter a year: "))

# A leap year is evenly divisible by 4, but not by 100
# If it is divisible by 4 and 100, it cannot be evenly divisible by 400
leap = not year % 4 and (year % 100 or not year % 400)

print('Leap year' if leap else 'Not leap year')
