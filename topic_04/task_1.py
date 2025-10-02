def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        raise ZeroDivisionError("Cannot divide by zero") from e

def get_number(prompt: str) -> float:
    while True:
        s = input(prompt)
        try:
            value = float(s)
            return value
        except ValueError:
            print("Invalid number. Please try again.")

def get_operator(prompt: str) -> str:
    valid_ops = {"+", "-", "*", "/"}
    while True:
        op = input(prompt).strip()
        if op in valid_ops:
            return op
        print(f"Invalid operator: {op}. Choose one of {valid_ops}.")

def calculator_loop():
    print("Calculator. Type 'exit' to quit at any prompt.")
    while True:
        cmd = input("Press Enter to continue or type 'exit' to quit: ").strip().lower()
        if cmd == "exit":
            print("Exiting program.")
            break

        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")
        op = get_operator("Enter operator (+, -, *, /): ")

        try:
            if op == "+":
                result = add(x, y)
            elif op == "-":
                result = subtract(x, y)
            elif op == "*":
                result = multiply(x, y)
            elif op == "/":
                result = divide(x, y)
            else:
                raise ValueError(f"Unsupported operator: {op}")

            print(f"Result: {result}")
        except ZeroDivisionError as zde:
            print("Error:", zde)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    calculator_loop()