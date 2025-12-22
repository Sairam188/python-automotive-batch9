class BankAccount:

    # initialization (constructor)
    def __init__(self, account_number, customer_name, initial_balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

        print(f"Current Balance: ₹{self.balance}")


# object creation
account1 = BankAccount("123", "Alice", 50.0)

# operations
account1.deposit(20)
account1.withdraw(30)
