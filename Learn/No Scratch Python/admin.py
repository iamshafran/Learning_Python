from user import User


class Admin(User):
    def __init__(self, title, first_name, last_name, age):
        super().__init__(title, first_name, last_name, age)
        self.privileges = Privileges(title, last_name)


class Privileges:
    def __init__(self, title, last_name):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        self.title = title.capitalize()
        self.last_name = last_name.capitalize()

    def show_privileges(self):
        print(
            f"{self.title} {self.last_name} is an admin with the following privileges:"
        )
        for privilege in self.privileges:
            print(privilege.title())
