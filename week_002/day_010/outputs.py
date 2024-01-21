# Function with Outputs

def format_name(f_name, l_name):
    """ This is how we use a docstring to explain what a defined function does. This must be declared on the first
    line right below the function."""
    if not f_name or not l_name:
        return "Nobody"

    return f"{f_name} {l_name}".lower().title()


print(format_name("oScaR", "crUz"))

print(format_name("", "crUz"))

