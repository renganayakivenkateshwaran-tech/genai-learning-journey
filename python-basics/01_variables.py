"""
Demonstration of Python variables, naming conventions, and data types.

Key Rules:
- Named memory locations for storing data.
- Should not be a Python keyword.
- No special characters are allowed except underscores (_).
"""


def demonstrate_variables() -> None:
    # Integer variable
    age: int = 34
    print(f"Age: {age}")

    # String variable using f-string interpolation
    name: str = "achu"
    print(f"My name is {name}")

    # Float variable
    gpa: float = 9.2
    print(f"GPA: {gpa}")


if __name__ == "__main__":
    demonstrate_variables()
