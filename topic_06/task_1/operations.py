import logging
from functions import add, subtract, multiply, divide

def get_numbers():
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))

            logging.info(f"User entered numbers: a={a}, b={b}")
            return a, b

        except ValueError:
            print("Please enter valid numbers!")
            logging.warning("Invalid number input")

def perform_operation():
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Your choice (1/2/3/4): ")

    logging.info(f"User selected operation: {choice}")

    if choice in ['1', '2', '3', '4']:
        a, b = get_numbers()

        if choice == '1':
            result = add(a, b)
            op = "Addition"
        elif choice == '2':
            result = subtract(a, b)
            op = "Subtraction"
        elif choice == '3':
            result = multiply(a, b)
            op = "Multiplication"
        elif choice == '4':
            result = divide(a, b)
            op = "Division"

        logging.info(f"{op} performed on {a} and {b}, result = {result}")
        print(f"Result: {result}")

    else:
        print("Invalid operation choice!")
        logging.warning(f"Invalid operation input: {choice}")