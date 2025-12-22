class BankAccount:

    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def is_senior_citizen(self):
        if self.age >= 60:
            return True
        return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")

    def calculate_compound_interest(self, years):
        if self.is_senior_citizen():
            rate = 8  # 8% per annum
            amount = self.balance * (1 + rate / 100) ** years
            return amount - self.balance
        else:
            return None

    def display_details(self):
        print("\nAccount Holder:", self.name)
        print("Age:", self.age)
        print("Balance:", round(self.balance, 2))


# -------- Main Program --------
try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    balance = float(input("Enter initial balance: "))
    years = int(input("Enter number of years: "))

    account = BankAccount(name, age, balance)
    account.display_details()

    ci = account.calculate_compound_interest(years)

    if ci is not None:
        print("Compound Interest:", round(ci, 2))
    else:
        print("Compound Interest is only for Senior Citizens")

except ValueError:
    print("Please enter valid numeric values")

except Exception:
    print("Something went wrong")
