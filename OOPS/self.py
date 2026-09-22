# why self keyword?
class Vehicle:
    def show(self): 
        print("Show Vehicle")

v = Vehicle() # creating and instance
v.show()

# When this code runs the interpreter automatically passes the current instance to the show method 
# which is "v" in this case -  but in class method we are not taking any argument

# So self is basically a - reference to the current instance being created or used 