def is_leap(year):
    # A leap year is evenly divisible by 4, but not by 100
    # If it is divisible by 4 and 100, it cannot be evenly divisible by 400
    return not year % 4 and (year % 100 or not year % 400)


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1] if not month == 2 else 29 if is_leap(year) else 28


year_input = int(input("Enter a year: "))
month_input = int(input("Enter a month: "))
days = days_in_month(year_input, month_input)
print(days)

