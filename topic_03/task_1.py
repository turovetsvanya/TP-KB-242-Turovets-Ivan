def calculator_match(x, y, op: str):
    match op:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            if y == 0:
                raise ValueError("Division by zero is impossible")
            return x / y
        case _:
            raise ValueError(f"Uknown: {op}")

def main():
    print("Calculator. Type 'exit' to quit.")
    while True:
        inp = input("Enter in format: number1 operator number2 - ")
        if inp.lower().strip() == "exit":
            print("Exiting program.")
            break
        parts = inp.split()
        if len(parts) != 3:
            print("Invalid format. Try again.")
            continue
        x_str, op, y_str = parts
        try:
            x = float(x_str)
            y = float(y_str)
            result = calculator_match(x, y, op)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()