# Calculate the average of the highs entered below
student_heights = "151 145 179 165 213"
student_heights = student_heights.split()

students = 0
total = 0

for h in student_heights:
    total += int(h)
    students += 1

print(f'Total Height: {total}')
print(f'Number of Students: {students}')
print(f'Average Height: {round(total / students)}')

