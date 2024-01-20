print("Welcome to the tip calculator.")

bill = float(input("Enter the total bill: $"))
tip_percentage = float(input("Enter your desired tip percentage: "))
amount_people = int(input("Enter the amount of people that will split the bill: "))

result = (bill * (1 + tip_percentage / 100)) / amount_people

result = "{:,.2f}".format(result)

print(f"Each person should pay: ${result}")