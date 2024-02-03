import pandas

result = []

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row['letter']: row['code'] for i, row in alphabet.iterrows()}


def generate_phonetic():
    word = list(input("Enter a word: ").replace(" ", "").strip().upper())

    if not word:
        print("Empty input")
        generate_phonetic()
        return

    try:
        print([alphabet[letter] for letter in word])
    except KeyError:
        print("Only letters in the alphabet and spaces may be used.")
        generate_phonetic()


generate_phonetic()
