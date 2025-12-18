import csv
import sys


class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class StudentList:
    def __init__(self):
        self.list_students = []

    def printAllList(self):
        for student in self.list_students:
            print(f"Student name is {student.name}, Phone is {student.phone}")

    def addNewElement(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")

        new_student = Student(name, phone)

        insert_position = 0
        for student in self.list_students:
            if name > student.name:
                insert_position += 1
            else:
                break

        self.list_students.insert(insert_position, new_student)
        print("New element has been added")

    def deleteElement(self):
        name = input("Please enter name to be deleted: ")
        delete_position = -1

        for student in self.list_students:
            if name == student.name:
                delete_position = self.list_students.index(student)
                break

        if delete_position == -1:
            print("Element was not found")
        else:
            self.list_students.pop(delete_position)
            print("Element has been deleted")

    def updateElement(self):
        name = input("Please enter name to be updated: ")
        name_update = input("Please enter new name for this student: ")

        delete_position = -1

        for student in self.list_students:
            if name == student.name:
                delete_position = self.list_students.index(student)
                break

        if delete_position == -1:
            print("Student is not found. Please try again correctly.")
            return

        phone_update = input("Please enter new phone for this student: ")

        self.list_students.pop(delete_position)

        new_student = Student(name_update, phone_update)

        insert_position = 0
        for student in self.list_students:
            if name_update > student.name:
                insert_position += 1
            else:
                break

        self.list_students.insert(insert_position, new_student)
        print("Element has been updated")


class Utils:
    @staticmethod
    def load_csv(file_name):
        try:
            with open(file_name, "r", newline='') as file:
                reader = csv.DictReader(file)
                group_list = StudentList()
                for row in reader:
                    student = Student(row["Name"], row["Phone"])
                    group_list.list_students.append(student)

            print("Data loaded successfully!")
            return group_list
        except FileNotFoundError:
            print("File not found!")

    @staticmethod
    def save_csv(group_list, file_name):
        with open(file_name, "w", newline='') as file:
            fieldnames = ["Name", "Phone"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in group_list.list_students:
                writer.writerow({
                    "Name": student.name,
                    "Phone": student.phone
                })
        return group_list


def main():
    if len(sys.argv) < 2:
        print("Please provide the file name as a command line argument!")
        return

    file_name = sys.argv[1]
    group_list = Utils.load_csv(file_name)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")

        match choice:
            case "C" | "c":
                group_list.addNewElement()
                group_list.printAllList()
            case "U" | "u":
                group_list.updateElement()
                group_list.printAllList()
            case "D" | "d":
                group_list.deleteElement()
                group_list.printAllList()
            case "P" | "p":
                group_list.printAllList()
            case "X" | "x":
                Utils.save_csv(group_list, file_name)
                print("CSV file is rewritten")
                print("Exit()")
                break
            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()