import pandas


# Tools
def print_line(amount):
    print("=" * amount)


# Pandas
data = pandas.read_csv("weather_data.csv")

print_line(100)

print(data)

print_line(100)

print(data['temp'])

print_line(100)

print(data.to_dict())

print_line(100)

print(data['temp'].tolist())

print_line(100)

# Calculate Average (Mean)

print(f"Average: {data['temp'].mean()}")

print_line(100)

# Calculate Max Value

print(f"Max: {data['temp'].max()}")

print_line(100)

# Highest Temperature of the Week

print(data[data['temp'] == data['temp'].max()])

print_line(100)

# Temperatures Above 15

print(data[data['temp'] > 15])

print_line(100)

# Rainy Days

print(data[data['condition'] == 'Rain'])

print_line(100)

# Convert Monday Temperature to Fahrenheit

print(f"Fahrenheit: {data[data['day'] == 'Monday']['temp'][0] * 9/5 + 32}")

print_line(100)

# Create Data Frame

students = {
    "students": ["Oscar", "Maya", "Ethan", "Isabella"],
    "scores": [100, 85, 77, 95]
}

students = pandas.DataFrame(students)

students.to_csv("students.csv", index=False)

print(pandas.read_csv("students.csv"))
