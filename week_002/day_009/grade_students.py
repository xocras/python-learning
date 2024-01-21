student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def grade(n):
    return "Outstanding" if n > 90 else "Exceeds Expectations" if n > 80 else "Acceptable" if n > 70 else "Fail"


student_grades = {}

for k, v in student_scores.items():
    student_grades[k] = grade(v)

print(student_grades)
