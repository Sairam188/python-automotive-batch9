class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"{self.student_id} - {self.name}")


# List of students (using tuple inside list)
students_data = [
    ("std_001", "Student1"),
    ("std_002", "Student2"),
    ("std_003", "Student3"),
    ("std_004", "Student4"),
    ("std_005", "Student5"),
    ("std_006", "Student6"),
    ("std_007", "Student7"),
    ("std_008", "Student8"),
    ("std_009", "Student9"),
    ("std_010", "Student10")
]

# Creating Student objects
students = [Student(sid, name) for sid, name in students_data]

print("Participants (Even Student IDs First):")
for student in students:
    if int(student.student_id.split("_")[1]) % 2 == 0:
        student.display()

print("\nRemaining Participants (Odd Student IDs):")
for student in students:
    if int(student.student_id.split("_")[1]) % 2 != 0:
        student.display()
