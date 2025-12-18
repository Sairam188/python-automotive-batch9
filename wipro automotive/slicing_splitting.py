#slicing=substring
myString="Hello World"
sub1=myString[0:5] #slice from index 0 to 5
sub2=myString[5:] #5th element to the end
sub3=myString[:5] # first 5 elements
sub4=myString[8] # 8th element from index 0
sub5=myString[-4:] #last 4 elements
print(sub1)
print(sub2)
print(sub3)
print(sub4)
print(sub5)

#in operator
if "l" in myString:
    print("l is in the string")

#splitting
words=myString.split(" ")
print(words)