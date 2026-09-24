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

my_new_car = Car('audi', 'a4', 2024)

print(my_new_car.get_description())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23 # Modifying attribute directly
my_new_car.read_odometer()

my_new_car.update_odometer(34)  # Modifying value using a function
my_new_car.read_odometer()

# You dont have to start from scratch when writing a class
# If the class you're writing is a specialized version of another class already written 
# Then we can use Inheritance
class ElectricCar(Car):
    """Represent aspects of car, specific to electric vehicles. """

    def __init__(self,make , model, year):
        """Initialize attributes of Parent class"""
        super().__init__(make,model,year) # The super function is a special function that allows you to call a method from the parent class
        


my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_description())