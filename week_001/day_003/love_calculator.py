print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

a, b, name = 0, 0, (name1 + name2).upper()

for c in "TRUE":
    a += name.count(c)

for c in "LOVE":
    b += name.count(c)

score = int(f'{a}{b}')

message = f'Your score is {score}'

if score < 10 or score > 90:
    message += ', you go together like coke and mentos.'
elif 40 <= score <= 50:
    message += ', you are alright together.'
else:
    message += '.'

print(message)
