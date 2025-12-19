import sys

# Reading numbers from command-line arguments
numbers = list(map(int, sys.argv[1:]))

# Calculating sum and average
total = sum(numbers)
average = total / len(numbers)

# Displaying results
print("Numbers entered :", numbers)
print("Sum:", total)
print("Average:", average)
