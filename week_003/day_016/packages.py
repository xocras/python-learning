# Packages
# https://pypi.org/

# Settings > Project > Python Interpreter

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type", ["Grass", "Fire", "Water"])

table.align = "l"

print(table)
