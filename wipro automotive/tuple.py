#tuple- collection which is ordered and unchangeable,used to group together related 

student=(21,"Bro","male")
print(student.count("Bro"))
print(student.index("male"))

for i in student:
    print(i)
if "Bro" in student:
    print("Bro is here")