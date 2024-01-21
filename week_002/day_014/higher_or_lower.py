import random

from rsc.data import data

VOWELS = [*"aeiou"]

game = True

score = 0


def display_item(compare, name, description, country):
    description = description[0].lower() + description[1:]

    print(f"\nCompare {compare}: {name}, a{'n' if description[0] in VOWELS else ''} {description}, from {country}")


def compare_followers():
    choice = input("\nWho has more followers? (A/B): ").lower()

    if choice == 'a':
        return a['follower_count'] > b['follower_count']
    if choice == 'b':
        return b['follower_count'] > a['follower_count']

    print("\nNot a valid choice...")
    compare_followers()


def choose_compare(x=None):
    y = random.choice(data)

    if not x:
        return y

    # Retry if the same object was selected
    if x.get('name', 0) == y.get('name', 0):
        choose_compare(x)

    return y


def check_answer(answer):
    if answer:
        return ["Correct!", 1]
    return ["Wrong!", 0]


while game:

    a = choose_compare()

    b = choose_compare(a)

    while a['name'] == b['name']:
        b = random.choice(data)

    display_item('A', a['name'], a['description'], a['country'])

    display_item('B', b['name'], b['description'], b['country'])

    result = compare_followers()

    result = check_answer(result)

    message = \
        f"{result[0]} " + \
        f"{a['name']} has {a['follower_count']} million followers and " + \
        f"{b['name']} has {b['follower_count']} million followers."

    score += result[1]

    print(f"\n{message}")

    if not result[1]:
        game = False
        print("\nYou lost.")

    print(f"\n{"Current" if game else "Final"} score: {score}")
