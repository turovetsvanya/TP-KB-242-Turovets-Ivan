students = [
    {"name": "Bob", "grade": 82},
    {"name": "Emma", "grade": 91},
    {"name": "Jon", "grade": 76},
    {"name": "Zak", "grade": 88}
]

sorted_by_name = sorted(students, key=lambda x: x["name"])

sorted_by_grade = sorted(students, key=lambda x: x["grade"])

print("Sorted by name:")
print(sorted_by_name)

print("\nSorted by grade:")
print(sorted_by_grade)