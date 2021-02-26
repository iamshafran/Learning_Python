class User:
    def __init__(self, title, first_name, last_name, age):
        self.title = title.capitalize()
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"{self.title} {self.first_name} {self.last_name} is {self.age} years old."
        )

    def greet_user(self):
        print(f"Hello {self.title} {self.last_name}, how are you doing today? \n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.login_attempts} login attempt(s) made.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(
            f"Login attempts reset successfully. Current login attempts = {self.login_attempts}"
        )


class Admin(User):
    def __init__(self, title, first_name, last_name, age):
        super().__init__(title, first_name, last_name, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(
            f"{self.title} {self.last_name} is an admin with the following privileges:"
        )
        for privilege in self.privileges:
            print(privilege.title())


admin1 = Admin("mr", "shafran", "nawaz", 33)

admin1.show_privileges()