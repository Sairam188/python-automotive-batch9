numbers = []
for i in range(1,11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
odd=0
even=0
for i in range(10):
    if numbers[i] % 2 == 0:
        even+=1
    else:
        odd+=1
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")