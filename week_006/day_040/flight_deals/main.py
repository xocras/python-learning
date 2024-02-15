# Flight Deals

from data_manager import DataManager


def main():
    # User input
    print("Welcome to Python's Flight Club")
    first_name = input("\nWhat's your first name?\n")
    last_name = input("\nWhat's your last name?\n")
    email = input("\nEnter your email:\n")
    email_confirmation = input("Confirm your email:\n")

    if email != email_confirmation:
        print("\nEmails don't match.")
        return

    print("\nSuccess! Your email has been added.")

    # Setup objects
    data_manager = DataManager()

    # Check existing users
    if email in [user['email'] for user in data_manager.get_users()]:
        print("\nYou're already in the club!")
        return

    # Add user
    parameters = {
        'user': {
            'firstName': first_name,
            'lastName': last_name,
            'email': email
        }
    }

    data_manager.add_user(parameters)


if __name__ == '__main__':
    main()
