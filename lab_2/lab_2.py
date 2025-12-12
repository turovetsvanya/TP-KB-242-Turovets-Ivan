import csv
from sys import argv

def load_students(file_name):
    students = []
    with open(file_name, "r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"Name": row["Name"], "Phone": row["Phone"]})
    return students

def save_students(file_name, students):
    with open(file_name, "w", newline='') as file:
        fieldnames = ["Name", "Phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def add_student(students, name, phone):
    students.append({"Name": name, "Phone": phone})

def find_student(students, name):
    for student in students:
        if student["Name"].lower() == name.lower():
            return student
    return None

def main():
    if len(argv) < 2:
        print("Please provide a CSV file to load data from.")
        return

    file_name = argv[1]

    students = load_students(file_name)
    print("Current student directory:")
    for s in students:
        print(f"{s['Name']} - {s['Phone']}")

    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Find a student")
        print("3. Exit and save")
        choice = input("Choose an action (1-3): ")

        if choice == "1":
            name = input("Enter student name: ")
            phone = input("Enter phone number: ")
            add_student(students, name, phone)
            print(f"{name} has been added to the directory.")
        elif choice == "2":
            name = input("Enter student name to find: ")
            student = find_student(students, name)
            if student:
                print(f"Found: {student['Name']} - {student['Phone']}")
            else:
                print("Student not found.")
        elif choice == "3":
            save_students(file_name, students)
            print(f"Data saved to {file_name}. Exiting.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()