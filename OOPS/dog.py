# Class -  it is basically a blueprint of something
# Object - it is an instance of a class

# how to create a class
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):          # __init__ method a special kind of method that runs automatically whenever new object is created
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    

# Making an instance (object)
my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")