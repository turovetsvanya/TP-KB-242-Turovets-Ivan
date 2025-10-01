import math
def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4 * a * c

def solve_quadratic(a: float, b: float, c: float):
    D = discriminant(a, b, c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        return None
    
a = int(input("What's A: "))
b = int(input("What's B: "))
c = int(input("What's C: "))
result = solve_quadratic(a, b, c)

if result is None:
    print("There are no result")
elif isinstance(result, tuple):
    print(f"x = {result[0]}, x2 = {result[1]}")
else:
    print(f"x = {result}")