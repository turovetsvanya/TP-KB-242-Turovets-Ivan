def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is impossible")
    return x / y

def calculator(x, y, op: str):
    if op == "+":
        return add(x, y)
    elif op == "-":
        return subtract(x, y)
    elif op == "*":
        return multiply(x, y)
    elif op == "/":
        return divide(x, y)
    else:
        raise ValueError(f"Uknown {op}")
    
x = float(input("Number 1: "))
y = float(input("Number 2: "))
op = input("Choose an action (+, -, *, /): ")

try:
    result = calculator(x, y, op)
    print(f"Result: {result}")
except Exception as e:
    print("Error: ", e)