class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def fill_gas_tank(self,gas):
        """The amount of gas can be filled in the tank"""
        self.gas = gas
        print(f"The amount of gas that can be filled in the tank is : {self.gas} Litres")


my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_description())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23 
my_new_car.read_odometer()

my_new_car.update_odometer(34)  
my_new_car.read_odometer()

my_new_car.fill_gas_tank(50)


# Compostion -  basically making a complex object with smaller and simple objects 
# Basically dividing a big complex solution into smaller ones

class Battery():
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size = 40):
        """Initialize the battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on full charge.")


class ElectricCar(Car):
    """Represent aspects of car, specific to electric vehicles. """

    def __init__(self,make , model, year):
        """Initialize attributes of Parent class"""
        super().__init__(make,model,year) # The super function is a special function that allows you to call a method from the parent class
        self.battery = Battery() # Instance as an attribute

    def fill_gas_tank(self):        # This is method override - defining a method in the child class with the same name as the parent class
        """Electric cars don't have gas tanks."""
        print("This car does'nt have a gas tank!")

my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_description())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()