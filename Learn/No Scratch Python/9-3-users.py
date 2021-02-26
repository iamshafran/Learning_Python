class User:
    def __init__(self, title, first_name, last_name, age):
        self.title = title.capitalize()
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.age = age

    def describe_user(self):
        print(
            f"{self.title} {self.first_name} {self.last_name} is {self.age} years old."
        )

    def greet_user(self):
        print(f"Hello {self.title} {self.last_name}, how are you doing today? \n")


user1 = User("mr", "john", "doe", 25)
user2 = User("miss", "jane", "doe", 20)
user3 = User("mrs", "julien", "denver", 45)


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()