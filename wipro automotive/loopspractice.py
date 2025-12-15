#Sum of the numbers
a,b=map(int,input("Enter Sum range").split(" "))
sum=0
for i in range(a,b):
    sum=sum+i
print(sum)

#Priniting Even numbers
print("Printing Even numbers")
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i%2==0:
        print(i,end = " ")

#Printing odd numbers
print("\n Printing odd numbers")
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i%2!=0:
        print(i,end=" ")

#Factorial of a number
num=int(input("Enter the number to find factorial"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("\n Factorial of given number ",factorial)


