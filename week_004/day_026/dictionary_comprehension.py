from random import randint

# Dictionary Comprehension

# Examples:

# {key:value for value in list}

# {key:value for value in list if true}

# {key:value for key,value in dictionary.items()}

# {key:value for value in dictionary.values()}

# {key:value for key in dictionary.keys()}

student_names = [
    "Emma Johnson", "Jackson Smith", "Olivia Williams", "Liam Brown", "Ava Davis",
    "Noah Miller", "Sophia Wilson", "Ethan Moore", "Isabella Taylor", "Lucas Anderson",
    "Mia Thomas", "Alexander Jackson", "Charlotte White", "James Harris", "Amelia Martin",
    "Benjamin Thompson", "Evelyn Garcia", "William Martinez", "Harper Robinson", "Michael Clark",
    "Abigail Rodriguez", "Daniel Lewis", "Emily Lee", "Matthew Walker", "Elizabeth Hall",
    "David Allen", "Ella Baker", "Jacob Turner", "Grace Adams", "Aiden Nelson",
    "Samantha Green", "Logan Carter", "Natalie King", "Ryan Scott", "Lily Hill",
    "John Wright", "Hannah Roberts", "Oliver Hughes", "Anna Cook", "Henry James",
    "Avery Murphy", "David Hill", "Ellie Reed", "Joseph Foster", "Nora Butler"
]

student_scores = {name: randint(0, 100) for name in student_names}

print(student_scores)

passed_students = {student: score for student, score in student_scores.items() if score >= 80}

print(passed_students)
