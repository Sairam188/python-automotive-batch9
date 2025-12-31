# Manager – Employee Performance Evaluation

# List of employees with manager and performance marks
employees = [
    ("E1", "M1", 80), ("E2", "M1", 70), ("E3", "M1", 90), ("E4", "M1", 60),
    ("E5", "M2", 85), ("E6", "M2", 75), ("E7", "M2", 95), ("E8", "M2", 65),
    ("E9", "M3", 78), ("E10", "M3", 88), ("E11", "M3", 92), ("E12", "M3", 68)
]

managers = ["M1", "M2", "M3"]

# Manager and their reportees (List Comprehension)
print("Manager and their Reportees:")
for m in managers:
    reportees = [e[0] for e in employees if e[1] == m]
    print(m, ":", reportees)

# Average performance of each manager's team
print("\nAverage Performance Score:")
for m in managers:
    scores = [e[2] for e in employees if e[1] == m]
    avg = sum(scores) / len(scores)
    print(m, ":", avg)

# High performers (score >= 80) using filter and lambda
print("\nHigh Performing Employees:")
high_performers = list(filter(lambda e: e[2] >= 80, employees))
for e in high_performers:
    print(e[0], "-", e[1], "-", e[2])
