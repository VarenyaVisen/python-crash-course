from car import ElectricCar

my_leaf = ElectricCar('Nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

# Module -  is basically a python file which stores multiple reusable classes and functions