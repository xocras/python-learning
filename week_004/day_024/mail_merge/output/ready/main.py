# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ready".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("../../input/letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("../../input/names/invited_names.txt") as file:
    invited_names = [name.strip() for name in file.readlines()]

for name in invited_names:
    output = starting_letter.replace(PLACEHOLDER, name)
    with open(f"./output/ready/letter_for_{name.lower()}.txt", mode="w") as file:
        file.write(output)
