#Student has to score min 60 percent in every subject to pass
def check_pass_fail(marks):
    for mark in marks:
        if mark < 60:
            return "Fail"
    return "Pass"


# Main Program
n = int(input("Enter number of subjects: "))

marks = []

for i in range(1, n + 1):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

result = check_pass_fail(marks)

print("Result:", result)
