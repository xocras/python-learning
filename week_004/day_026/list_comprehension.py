# List Comprehension

odds = [n for n in range(11) if n % 2]

even = [n for n in range(11) if not n % 2]

name = [character.upper() for i, character in enumerate("Oscar") if not i % 2]

name = "".join(name)

print([odds, even])

print(name)

