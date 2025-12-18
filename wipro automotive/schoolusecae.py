# List of 20 students (name, surname)
students = [
    ("Ravi", "Kumar"),("Anil", "Sharma"),("Ravi", "Verma"),("Sita", "Reddy"), ("Anil", "Gupta"), ("Kiran", "Patel"),
    ("Pooja", "Singh"),("Rahul", "Mehta"),("Sita", "Rao"),("Amit", "Jain"),("Neha", "Malik"),("Vijay", "Iyer"),
    ("Amit", "Agarwal"),("Sunil", "Das"),("Kiran", "Joshi"),("Ramesh", "Nair"),("Pooja", "Chopra"),
    ("Deepak", "Bansal"),("Neha", "Kapoor"),("Manoj", "Pandey")
]

unique_students = []
seen_names = set()

for name, surname in students:
    if name not in seen_names:
        unique_students.append((name, surname))
        seen_names.add(name)

print("Students after removing duplicate names:")
for student in unique_students:
    print(student)
print("number of unique students:",len(unique_students))