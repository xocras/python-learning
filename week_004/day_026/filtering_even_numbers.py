# Filtering Even Numbers

# '1, 1, 2, 3, 5, 8, 13, 21, 34, 55'

list_of_strings = input().split(',')

list_of_numbers = [int(s) for s in list_of_strings]

result = [n for n in list_of_numbers if not n % 2]

print(result)