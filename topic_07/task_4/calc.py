from operations import OperationHandler

class CalculatorApp:
    def __init__(self):
        self.handler = OperationHandler()

    def run(self):
        print("Simple OOP Calculator")
        while True:
            self.handler.perform_operation()
            cont = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Thank you for using the calculator!")
                break

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()