# BMI Calculator
height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    message = 'you are underweight.'
elif bmi < 25:
    message = 'you have a normal weight.'
elif bmi < 30:
    message = 'you are slightly overweight.'
elif bmi < 35:
    message = 'you are obese.'
else:
    message = 'you are clinically obese.'

bmi = "{:,.2f}".format(bmi)

print(f"Your BMI is {bmi}, {message}")
