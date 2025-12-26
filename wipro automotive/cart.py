# -------------------------------
# Base class
# -------------------------------
class Discount:
    def apply_discount(self, amount):
        return amount   # No discount by default


# -------------------------------
# Seasonal Discount (10%)
# -------------------------------
class SeasonalDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.90


# -------------------------------
# Festival Discount (20%)
# -------------------------------
class FestivalDiscount(Discount):
    def apply_discount(self, amount):
        return amount * 0.80


# -------------------------------
# Coupon Discount (Flat ₹2000)
# -------------------------------
class CouponDiscount(Discount):
    def apply_discount(self, amount):
        return amount - 2000


# -------------------------------
# Store Class
# -------------------------------
class Store:
    def __init__(self):
        self.items = {
            1: ("Apple iPhone 17 (512 GB)", 102900),
            2: ("SONY BRAVIA 55 inch 4K TV", 57990),
            3: ("Mivi Fort H880 Soundbar", 9999),
            4: ("Wakefit Sofa Cum Bed", 12148),
            5: ("SONY PlayStation 5 Digital", 44990)
        }

    def show_items(self):
        print("\nAvailable Items:")
        for key, value in self.items.items():
            print(f"{key}. {value[0]} - ₹{value[1]}")

    def get_price(self, choice):
        return self.items[choice][1]


# -------------------------------
# Checkout Process
# Polymorphism used here
# -------------------------------
store = Store()
total_price = 0

store.show_items()

while True:
    try:
        choice = int(input("\nEnter item number: "))
        price = store.get_price(choice)
        total_price += price

        more = input("Add more items? (yes/no): ").lower()
        if more != "yes":
            break
    except:
        print("Invalid input, try again.")

print("\nTotal Amount: ₹", total_price)

# -------------------------------
# Discount Selection
# -------------------------------
print("\nChoose Discount Type:")
print("1. Seasonal Discount (10%)")
print("2. Festival Discount (20%)")
print("3. Coupon Discount (₹2000 off)")

discount_choice = int(input("Enter discount choice: "))

if discount_choice == 1:
    discount = SeasonalDiscount()
elif discount_choice == 2:
    discount = FestivalDiscount()
elif discount_choice == 3:
    discount = CouponDiscount()
else:
    discount = Discount()

final_price = discount.apply_discount(total_price)

print("\n----- BILL DETAILS -----")
print("Original Price: ₹", total_price)
print("Final Price after Discount: ₹", int(final_price))
