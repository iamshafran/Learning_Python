class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")


dominos = Restaurant("dominos", "pizza")

print(dominos.restaurant_name)
print(dominos.cuisine_type)

dominos.describe_restaurant()
dominos.open_restaurant()