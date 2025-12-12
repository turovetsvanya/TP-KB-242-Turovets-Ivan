from functions import Calculator

class OperationHandler:

    def __init__(self):
        self.calc = Calculator()

    def get_numbers(self):
        while True:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                return a, b
            except ValueError:
                print("Please enter valid numbers!")

    def perform_operation(self):
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)\n")

        choice = input("Your choice (1/2/3/4): ").strip()

        if choice in ('1', '2', '3', '4'):
            a, b = self.get_numbers()
            if choice == '1':
                print(f"Result: {self.calc.add(a, b)}")
            elif choice == '2':
                print(f"Result: {self.calc.subtract(a, b)}")
            elif choice == '3':
                print(f"Result: {self.calc.multiply(a, b)}")
            elif choice == '4':
                print(f"Result: {self.calc.divide(a, b)}")
        else:
            print("Invalid operation choice!")