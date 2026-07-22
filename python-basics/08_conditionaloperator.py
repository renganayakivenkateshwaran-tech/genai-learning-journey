"""
Demonstration of Conditional (Ternary) Operators in Python.

Syntax:
    value_if_true if condition else value_if_false
"""


def demonstrate_conditional_operator() -> None:
    a: int = 3
    b: int = 5

    # 1. Basic Value Selection
    min_value: int = a if a < b else b
    print(f"Minimum value between {a} and {b}: {min_value}")

    # 2. Check Even or Odd
    parity: str = "EVEN" if a % 2 == 0 else "ODD"
    print(f"The number {a} is: {parity}")

    # 3. User Role Authorization Check
    user: str = "admin"
    access_level: str = "Full Access" if user == "admin" else "Limited Access"
    print(f"User Status ({user}): {access_level}")

    # 4. Authentication Check using F-Strings
    name: str = "USER7675"
    password: str = "12311109876"
    
    auth_result: str = f"Welcome, {name}!" if password == "12311109876" else "Incorrect password! Try Again."
    print(f"Auth Check: {auth_result}")


if __name__ == "__main__":
    demonstrate_conditional_operator()
