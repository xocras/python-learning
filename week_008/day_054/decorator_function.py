# A decorator functions is just a functions that wraps another function
# in order to give it some additional functionality

def welcome(function):
    def welcome_user():
        function()
        print('Welcome to Python!')
    return welcome_user


@welcome
def greet():
    print('Hello World!')


greet()
