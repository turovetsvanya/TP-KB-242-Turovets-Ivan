from functions import add, subtract, multiply, divide

def get_numbers():
    a = float(input("1st number: "))
    b = float(input("2nd number: "))
    return a, b

def calculate():
    print("Choose operation:")
    print("1 - Addition (+)")
    print("2 - Subtraction (-)")
    print("3 - Multiplication (*)")
    print("4 - Division (/)")

    choice = input("Your choice: ")

    a, b = get_numbers()

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice.")