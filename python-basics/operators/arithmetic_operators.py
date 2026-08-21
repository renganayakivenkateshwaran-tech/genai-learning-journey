"""
Demonstration of Arithmetic Operators in Python.

Operators Covered:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Floor Division (//)
- Modulus (%)
- Exponentiation (**)
"""


def demonstrate_arithmetic_operators() -> None:
    a: int = 5
    b: int = 5

    # 1. Addition
    print(f"Addition ({a} + {b}): {a + b}")

    # 2. Subtraction
    print(f"Subtraction ({a} - {b}): {a - b}")

    # 3. Multiplication
    print(f"Multiplication ({a} * {b}): {a * b}")

    # 4. Division (returns float)
    print(f"Division ({a} / {b}): {round(a / b, 2)}")

    # 5. Floor Division (returns integer quotient)
    print(f"Floor Division ({a} // {b}): {a // b}")

    # 6. Modulus (returns remainder)
    print(f"Modulus ({a} % {b}): {a % b}")

    # 7. Exponentiation (power)
    print(f"Exponentiation ({a} ** {b}): {a ** b}")


if __name__ == "__main__":
    demonstrate_arithmetic_operators()
