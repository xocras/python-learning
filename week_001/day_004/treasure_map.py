# Build Treasure Map
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

treasure_map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put the treasure?: ").upper()

keys = {'A': 0, 'B': 1, 'C': 2}

# Assign Chosen Tile
treasure_map[int(position[1])-1][keys[position[0]]] = 'X'

# Print Treasure Map
print(f"{line1}\n{line2}\n{line3}")
