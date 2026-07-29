"""
Demonstration of *args (Arbitrary Positional Arguments) in Python.

Concepts Covered:
- Accepting a dynamic number of positional arguments
- Packing extra positional arguments into a Tuple
- Iterating over *args and using built-in operations
"""


# 1. Summing Any Number of Arguments
def add(*numbers: float) -> float:
    # Option A: Manual accumulation loop
    total: float = 0.0
    for num in numbers:
        total += num
    return total

    # Option B (Pythonic): return sum(numbers)


# 2. Printing Any Number of Names
def print_names(*names: str) -> None:
    for name in names:
        print(name, end=" ")
    print()  # Newline after printing names


def demonstrate_args() -> None:
    # Example 1: Summing Numbers
    print("--- 1. Variable Positional Arguments (Math) ---")
    result_three = add(9, 2, 3)
    result_five = add(10, 20, 30, 40, 50)
    print(f"Sum of (9, 2, 3): {result_three}")
    print(f"Sum of (10, 20, 30, 40, 50): {result_five}\n")

    # Example 2: Printing Names
    print("--- 2. Variable Positional Arguments (Strings) ---")
    print("Names list: ", end="")
    print_names("Achu", "Bala", "Yami", "Kavi", "Priya")


if __name__ == "__main__":
    demonstrate_args()
