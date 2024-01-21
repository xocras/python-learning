# Functions

# Parameter:
# What you need to pass into the function.
# It is declared at the moment you define a function.

# Argument:
# What you pass into the function.
# It is passed at the moment you call the function.

def greet():
    print("\nHello World!")


def greet_user(name):
    print(f"\nHello, {name}!")


def how_is_it(name, location):
    greet()
    greet_user(name)
    print(f"How is it in {location}?")


# Positional Argument
how_is_it("Oscar", "Santo Domingo")

# Keyword Arguments
how_is_it(location="Santo Domingo", name="Oscar")
