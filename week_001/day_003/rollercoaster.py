print("Welcome to the roller-coaster!")


def check_rider():
    min_height = 120

    height = float(input("Enter your height (cm): "))

    if height > min_height:
        print("You can ride the roller-coaster!")
    else:
        print(f"You need to be at least {min_height}cm to ride the roller-coaster.")
        return

    prices = [[12, 5], [19, 7]]

    age = int(input("What's your age?: "))

    bill = next((b for a, b in prices if age < a), 12)

    bill = 0 if 45 < age < 50 else bill

    photo = input("Would you like a photo taken? (Y/N): ").upper()

    photo_price = 3

    bill = (bill + photo_price) if photo == "Y" else bill

    bill = "{:,.2f}".format(bill)

    print(f"Your total bill is: ${bill}")


check_rider()
