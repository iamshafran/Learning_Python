class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")


dominos = Restaurant("dominos", "pizza")
cochin = Restaurant("cochin", "indian")
prezzo = Restaurant("prezzo", "italian")

dominos.describe_restaurant()
cochin.describe_restaurant()
prezzo.describe_restaurant()