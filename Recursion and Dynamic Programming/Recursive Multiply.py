# Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.


# Brute Force Recursive Multiplication
def recursive_multiply_brute(a, b):
    if b == 0:
        return 0
    return a + recursive_multiply_brute(a, b - 1)

# Example usage
a = 5
b = 3
print(f"Brute Force Multiply: {recursive_multiply_brute(a, b)}")  # Output: 15
