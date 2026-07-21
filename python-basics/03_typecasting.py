"""
Python Basics: Simple Beginner Example

Concepts Covered:
1. Variables & Data Types
2. User Input & Direct Type Casting
3. Conditional Logic (If / Else)
4. Formatted Strings (f-strings)
"""


def main() -> None:
    print("=== Welcome to the Python Basics Demo ===\n")

    # 1. User Input & Strings
    name: str = input("Enter your name: ")
    print(f"Hello, {name}!\n")

    # 2. Direct Type Casting (String to Int)
    age: int = int(input("Enter your age: "))

    # 3. Direct Type Casting (String to Float)
    gpa: float = float(input("Enter your GPA (0.0 - 4.0): "))

    print("\n--- Summary ---")

    # 4. Math Operations
    next_year_age: int = age + 1
    print(f"Name: {name}")
    print(f"Current Age: {age} (Next year you will be {next_year_age})")
    print(f"GPA: {gpa}")

    # 5. Conditional Logic (If / Else)
    if age >= 18:
        is_adult: bool = True
        status: str = "Adult"
    else:
        is_adult: bool = False
        status: str = "Minor"

    print(f"Status: {status} (Is Adult: {is_adult})")


if __name__ == "__main__":
    main()
