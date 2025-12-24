class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    #Printing our string object
    def __repr__(self):
        return f"{self.brand} {self.model}"

    def move(self):
        print("drive")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")

class Truck:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("turn with more mileage")

car=Car("ford","figo")
boat=Boat("Ibita","I20")
truck=Truck("Tata","T20")

for x in (car,boat,truck):
    x.move()

