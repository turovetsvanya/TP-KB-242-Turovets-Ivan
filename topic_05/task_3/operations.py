from functions import add, subtract, multiply, divide

def get_numbers():
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            return a, b
        except ValueError:
            print("Please enter valid numbers!")

def perform_operation():
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        a, b = get_numbers()
        if choice == '1':
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {divide(a, b)}")
    else:
        print("Invalid operation choice!")