class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

students = [
    Student("Max", 18),
    Student("Anna", 19),
    Student("Bohdan", 17),
    Student("Maria", 20)
]

while True:
    column = input("Sort by 'name' or 'age'? ").strip().lower()
    if column in ("name", "age"):
        break
    print("Invalid input. Please enter 'name' or 'age'.")

if column == "name":
    sorted_students = sorted(students, key=lambda s: s.name)
else:
    sorted_students = sorted(students, key=lambda s: s.age)

print(f"\nStudents sorted by {column}:")
for s in sorted_students:
    print(s)