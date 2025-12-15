#palindrome 
num=int(input("Enter the number to check palindrome"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("Palindrome")
else:
    print("Not Palindrome")
    
