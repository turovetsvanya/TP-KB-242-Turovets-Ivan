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

x = float(input("Number 1: "))
y = float(input("Number 2: "))
op = input("Chose an action (+, -, *, /): ")

try:
    result = calculator_match(x, y, op)
    print (f"Result: {result}")
except Exception as e:
    print ("Error: ", e)