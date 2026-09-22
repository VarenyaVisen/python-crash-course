class Vehicle:

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def details(self):
        print(f"{self.model} has {self.engine} engine!")

v1 = Vehicle("Lamborghini", "8-stroke")
v1.details()

v2 = Vehicle("Ferrari", "7-stroke")
v2.details()

print(v1,v2)