# BMI Calculator
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

result = weight / (height ** 2)

print(f"Your BMI is: {result}")
