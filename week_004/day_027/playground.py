# Arguments
def add(*numbers):
    print(sum(numbers))


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Keyword Arguments
def greet(**names):
    print(' '.join(names.values()))


greet(first_name="Oscar", last_name="Cruz")


# Keyword Arguments - Classes
class Car:
    def __init__(self, **components):
        self.brand = components.get("brand")
        self.doors = components.get("Doors")
        self.wheels = components.get("wheels")

    def list_properties(self):
        print(f"Brand: {self.brand}")
        print(f"Doors: {self.doors}")
        print(f"Wheels: {self.wheels}")


car = Car(wheels=4, brand="Toyota")

car.list_properties()