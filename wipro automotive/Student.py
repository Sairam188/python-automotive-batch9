import person 
class Student(Person):
    #pass
    def _init_(self,fname,lname,year):
       #add prop here
       #Person.__init(self,fname,lname)
       super().__init__(fname,lname)
       self.year=year

    def welcome(self):
        print("Welcome")

x=student("a","b",2025)
x.printname()