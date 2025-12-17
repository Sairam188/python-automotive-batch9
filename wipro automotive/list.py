#List = used to store multiple items in a single variable
#List items are ordered, changeable, and allow duplicate values.

places=["Delhi","Mumbai","Hyderabad","Kolkata","Pune"]

print(places[0])
print(places[-1])
places[0]="Chennai"
print(places[0])


places.append("Kerala")
places.remove("Hyderabad")
places.pop() #removes last element
places.pop(1) #removes element at index 1
places.insert(0,"Bangalore")
places.sort()

#for i in places:
#   print(i)

print(places)