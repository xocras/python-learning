# Data Overlap
with open("file1.txt") as file:
    a = [int(n.strip()) for n in file.readlines()]

with open("file2.txt") as file:
    b = [int(n.strip()) for n in file.readlines()]

result = [n for n in a if n in b]

print(result)
