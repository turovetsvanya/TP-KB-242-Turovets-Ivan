def reverse_string(text: str) -> str:
    return text [::-1]
s = "Hello, World!"
print("Original:", s)
print("Reverse", reverse_string(s))