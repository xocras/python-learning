# Global Scope
enemies = ["Skeletons", "Bats"]

print(enemies)


def list_enemies():
    # Function Scope
    # noinspection PyShadowingNames
    enemies = ["Rats", "Slimes"]
    print(enemies)


list_enemies()


