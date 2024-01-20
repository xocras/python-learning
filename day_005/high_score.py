# Find the highest score of the list of scores entered below
student_scores = "78 65 89 86 55 91 64 89"
student_scores = student_scores.split()

max_score = 0

for score in student_scores:
    max_score = int(score) if int(score) > max_score else max_score

print(f'The highest score in the class is: {max_score}')