# main.py

import calculatorfunctions

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1-4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print("Result:", calculatorfunctions.add(num1, num2))
elif choice == 2:
    print("Result:", calculatorfunctions.subtract(num1, num2))
elif choice == 3:
    print("Result:", calculatorfunctions.multiply(num1, num2))
elif choice == 4:
    print("Result:", calculatorfunctions.divide(num1, num2))
else:
    print("Invalid choice")
