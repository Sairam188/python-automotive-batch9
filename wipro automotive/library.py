class Library:

    # constructor
    def __init__(self, name, total_books):
        self.name = name
        self.total_books = total_books

    def display(self):
        print("Library Name:", self.name)
        print("Total Books:", self.total_books)
        print()

    def issue_book(self, count):
        if count <= self.total_books:
            self.total_books -= count
            print(f"{count} book(s) issued from {self.name}")
        else:
            print("Not enough books available")

    def return_book(self, count):
        self.total_books += count
        print(f"{count} book(s) returned to {self.name}")
        print()


# object creation
lib1 = Library("Central Library", 500)
lib2 = Library("College Library", 300)
lib3 = Library("City Library", 200)

# method calls
lib1.display()
lib1.issue_book(10)
lib1.return_book(5)

lib2.display()
lib2.issue_book(20)
lib2.return_book(10)

lib3.display()
lib3.issue_book(15)
lib3.return_book(5)
