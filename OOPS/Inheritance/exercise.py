class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["vanilla","chocolate","black currant", "butterscotch"]

    def display_flavors(self):
        print("Available Ice Cream flavors : ")
        for flavor in self.flavors:
            print(f"-{flavor}")


ice_cream_stand = IceCreamStand("Varenya's Ice Cream", "dessert")

ice_cream_stand.display_flavors()