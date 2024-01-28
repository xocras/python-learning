# The 'with' keyword will automatically close the opened file
# Preventing any accidents regarding the computer resources

# Modes:
# 'r' - read
# 'w' - write (replaces everything)
# 'a' - append

with open("hello.txt", mode="w") as file:

    file.write("Hello World!")

with open("data.txt", mode="a") as file:

    file.write("\n\n- Python 3.12")

with open("data.txt", mode="r") as file:

    text = file.read()

    print(text)
