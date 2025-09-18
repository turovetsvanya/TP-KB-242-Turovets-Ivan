def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c
a, b, c = 1, 2, 3
D = discriminant(a, b, c)
print(f"discriminant = {D}")