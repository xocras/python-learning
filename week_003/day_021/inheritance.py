class Animal:
    def __init__(self, message):
        self.message = message

    def talk(self):
        print(self.message)


class Dog(Animal):
    def __init__(self, message):
        super().__init__(message)
        self.sound = "Woof, woof!"

    def bark(self):
        print(self.sound)

    def talk(self):
        super().talk()
        print("Wait... Dogs can't talk!")


doggy = Dog("Hello World!")

doggy.bark()
doggy.talk()
