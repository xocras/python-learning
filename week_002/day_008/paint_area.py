import math


def paint_calc(height, width, coverage):
    cans = math.ceil(height * width / coverage)
    print(f"You'll need {cans} cans of paint.")


h = int(input("Height of wall (m): "))
w = int(input("Width of wall (m): "))

# How many m^2 are covered by can of paint:
c = 5

paint_calc(height=h, width=w, coverage=c)
