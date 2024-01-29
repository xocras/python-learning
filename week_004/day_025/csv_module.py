import csv

# CSV
with open("weather_data.csv") as file:
    temperatures = [row[1] for row in csv.reader(file)][1:]

print(temperatures)
