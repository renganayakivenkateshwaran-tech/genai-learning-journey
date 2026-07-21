"""
Demonstration of User Input and Output operations in Python
"""


def demonstrate_input_output() -> None:
    # 1. Single Input & String Output
    name: str = input("What is your name? ")
    print(f"Hello, {name}!")

    # 2. Multiple Inputs on One Line
    # split() separates input strings by spaces by default
    x, y = input("Enter two values (separated by space): ").split()
    print(f"First value: {x}")
    print(f"Second value: {y}")


if __name__ == "__main__":
    demonstrate_input_output()
