"""
Demonstration of While Loops in Python.

Concepts Covered:
- Counter-based while loops
- Generating math tables using while loops
- Input validation (Password authentication)
- Range validation (Age checks)
"""


def demonstrate_while_loops() -> None:
    # 1. Basic Counter Loop (0 to 10)
    print("--- 1. Basic Counter Loop ---")
    num: int = 0
    while num <= 10:
        print(num)
        num += 1
    print()

    # 2. Multiplication Table (3s Table)
    print("--- 2. Multiplication Table (3s) ---")
    num = 1
    while num <= 10:
        print(f"3 x {num} = {num * 3}")
        num += 1
    print()

    # 3. Password Validation Loop
    print("--- 3. Password Authentication ---")
    password: str = "python123"
    user_pwd: str = input("Enter the password: ")

    while user_pwd != password:
        print("Incorrect password!")
        user_pwd = input("Enter the correct password: ")

    print("Welcome!\n")

    # 4. Age Range Validation Loop
    print("--- 4. Age Range Check ---")
    age: int = int(input("Enter your age: "))

    while age < 18 or age > 100:
        print("Too old or too young!")
        age = int(input("Enter your correct age: "))

    print("Welcome to our website!")


if __name__ == "__main__":
    demonstrate_while_loops()
