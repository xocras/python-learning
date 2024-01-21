from functools import reduce

alphabet = [*"abcdefghijklmnopqrstuvwxyz"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
t = input("\nType your message:\n").lower()
s = int(input("\nType the shift number:\n"))


def encrypt(text, shift):
    word = \
        reduce(lambda a, b: a + (alphabet[(alphabet.index(b) + shift) % 26] if b in alphabet else b), text, '')

    print(f"\nHere's your encoded message: \n{word}")


def decrypt(text, shift):
    word = \
        reduce(lambda a, b: a + (alphabet[(alphabet.index(b) - shift)] if b in alphabet else b), text, '')

    print(f"\nHere's your decoded message: \n{word}")


encrypt(t, s) if direction == 'encode' else decrypt(t, s)
