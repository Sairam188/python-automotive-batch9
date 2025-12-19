# Importing both functions from the same file
from mulanddiv import multiply, divide

def calculate_simple_interest():
    # Taking user input
    p = float(input("Enter Principal amount: "))
    r = float(input("Enter Rate of Interest: "))
    t = float(input("Enter Time (in years): "))

    # Using imported multiplication function
    product = multiply(p, r, t)

    # Using imported division function
    si = divide(product, 100)

    print("Simple Interest is:", si)

# Function call
calculate_simple_interest()
