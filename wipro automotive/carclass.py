class Car:

    # constructor
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print()

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    # new function 1
    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

    # new function 2
    def apply_discount(self, percent):
        discount = (self.price * percent) / 100
        self.price -= discount
        print(f"Price after {percent}% discount: {self.price}")
        print()


# object creation
car1 = Car("Honda", "City", 1200000)
car2 = Car("Toyota", "Innova", 2000000)
car3 = Car("Hyundai", "i20", 900000)

# method calls

car3.start()
car3.stop()

car1.display()
car1.apply_discount(10)

car2.display()
car2.apply_discount(20)





