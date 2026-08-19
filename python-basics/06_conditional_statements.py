"""
Demonstration of Conditional Statements in Python.

Concepts Covered:
- Simple if-else branching
- Multi-condition branching using elif
- String length validation and membership checks
"""


def demonstrate_condition_statements() -> None:
    # 1. Simple If-Else Statement (Voting Eligibility)
    age: int = int(input("What's your age? "))
    
    if age >= 18:
        print("You are eligible for voting.")
    else:
        print("You are NOT eligible for voting.")

    print("\n--- Name Validation ---")

    # 2. Elif Statements (Name Length & Character Validation)
    name: str = input("What's your name? ")

    if len(name) < 4:
        print("Too short")
    elif "." in name or " " in name:
        print("Not valid")
    elif len(name) > 12:
        print("Only 12 characters are allowed")
    else:
        print("Welcome!")


if __name__ == "__main__":
    demonstrate_condition_statements()
