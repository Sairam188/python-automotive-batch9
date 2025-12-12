#Armstrong number

num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
#Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
