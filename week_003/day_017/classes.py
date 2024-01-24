# Classes
class User:
    def __init__(self, data):
        self.id = data.get("id", "000")
        self.name = data.get("name", "Undefined")
        self.followers = data.get("followers", [])
        self.following = data.get("following", [])

    def display_information(self):
        print(f"\nID: {self.id} - {self.name} | {len(self.followers)} followers | {len(self.following)} following")

    def display_followers(self):
        print(f"Followers: {self.followers}")

    def display_following(self):
        print(f"Following: {self.following}")

    def follow(self, user):
        user.followers.append(self.name)
        self.following.append(user.name)


user_1 = User({
    "id": "001",
    "name": "Oscar"
})
user_2 = User({})

user_2.follow(user_1)

user_1.display_information()
user_1.display_followers()
user_1.display_following()

user_2.display_information()
user_2.display_followers()
user_2.display_following()



