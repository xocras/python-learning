print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 15 if size == 'S' else 20 if size == 'M' else 25

bill += 0 if add_pepperoni == 'N' else 2 if size == 'S' else 3

bill += 1 if extra_cheese == 'Y' else 0

bill = "{:,.2f}".format(bill)

print(f'Your final bill is: ${bill}.')
