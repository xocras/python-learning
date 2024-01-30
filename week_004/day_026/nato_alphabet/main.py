import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row['letter']: row['code'] for i, row in alphabet.iterrows()}

word = list(input("Enter a word: ").replace(" ","").strip().upper())

print([alphabet[letter] for letter in word])
