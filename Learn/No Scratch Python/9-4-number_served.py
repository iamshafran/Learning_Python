class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


restaurant = Restaurant("dominos", "pizza")
print(restaurant.number_served)

restaurant.set_number_served(15)
print(restaurant.number_served)

restaurant.increment_number_served(20)
print(restaurant.number_served)