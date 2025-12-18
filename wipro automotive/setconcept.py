myset={"apple","banana","cherry","apple",True,1,2,False,0}
print(myset)
#True is 1 so duplicate 1 not printed,False is 0 so duplicate 0 not printed
myset2={"a","n"}

emptyset=set()
emptydic={ }
print(type(emptyset))
myset.add(10)
myset.discard(10)
 
mylist=['a','b']
myset.update(mylist)
# myset.append("grapes") #error
count=len(myset)
print(myset|myset2) #union
print(myset&myset2) #intersection

for fruit in myset:
    print(fruit)
