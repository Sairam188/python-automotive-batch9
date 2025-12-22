# class -> keyword to define a new class
class Dog:
    # constructor (runs when object is created)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # behavior of Dog class
    def bark(self):
        print(f"{self.name} doesn't bark!")


# objects (instances of Dog class)
dog1 = Dog("Lucy", 4)
dog2 = Dog("Test", 3)

# calling methods
dog1.bark()
dog2.bark()
