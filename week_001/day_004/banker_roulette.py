import random

# Choose someone randomly from the list of names below
names = "Angela, Ben, Jenny, Michael, Chloe"

names = names.split(", ")

i = random.randint(1, len(names)) - 1

print(f'{names[i]} is going to buy the meal today!')
