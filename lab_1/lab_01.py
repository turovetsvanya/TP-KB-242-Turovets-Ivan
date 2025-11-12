## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567"},
    {"name":"Emma", "phone":"0631234567"},
    {"name":"Jon",  "phone":"0631234567"},
    {"name":"Zak",  "phone":"0631234567"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"]
        if "email" in elem:
            strForPrint += ",  Email is " + elem["email"]
        if "group" in elem:
            strForPrint += ",  Group is " + elem["group"]

        print(strForPrint)
    return

def addNewElement():
    name = input("PeІase enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email (or leave empty): ")
    group = input("Please enter student group (or leave empty): ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    found = False

    for item in list:
            print(f"Current data: {item}")
            new_name = input("Enter new name (leave empty to keep current): ")
            new_phone = input("Enter new phone (leave empty to keep current): ")
            new_email = input("Enter new email (leave empty to keep current): ")
            new_group = input("Enter new group (leave empty to keep current): ")

            # Update only provided fields
            if new_name != "":
                item["name"] = new_name
            if new_phone != "":
                item["phone"] = new_phone
            if new_email != "":
                item["email"] = new_email
            if new_group != "":
                item["group"] = new_group

            # Re-sort list after updating name
            list.sort(key=lambda x: x["name"])
            found = True
            print("Student information updated successfully.")
            break

    if not found:
        print("Student not found.")
    return
    # implementation required

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")


main()