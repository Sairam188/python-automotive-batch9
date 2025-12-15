# Student Marks Analysis

# Taking Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculating total marks
total_marks = sum(marks)

# Calculating percentage
percentage = (total_marks / 500) * 100

# Determining grade
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Displaying results
print("\n Student Result Analysis")
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)

# Store results in a file
with open("student_result.txt", "w") as file:
    file.write("Student Marks Analysis\n")
    file.write(f"Marks: {marks}\n")
    file.write("Total Marks:" + str(total_marks) + "\n" )
    file.write(f"Percentage: {percentage:.2f}%\n")
    file.write(f"Grade: {grade}\n")

print("\n Results saved successfully in 'student_result.txt'")
