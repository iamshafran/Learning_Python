class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 10

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry", "rocky road"]

    def flavors_served(self):
        print(f"{self.restaurant_name} serves the following flavors:")
        for flavor in self.flavors:
            print(flavor.title())
