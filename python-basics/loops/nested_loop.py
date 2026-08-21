"""
Demonstration of Nested Loops in Python.

Concepts Covered:
- 2D Grid Iteration (Outer loop for rows, Inner loop for columns)
- Pattern Printing (Inverted Right-Angled Triangle)
- Matrix / Multiplication Table Generation
"""


def demonstrate_nested_loops() -> None:
    # 1. Repeated Range Iteration
    print("--- 1. Simple Grid Iteration ---")
    for y in range(0, 2):
        for x in range(0, 5):
            print(x, end=", ")
        print()  # Newline after inner loop completes
    print()

    # 2. Inverted Star Pattern with Leading Spaces
    print("--- 2. Inverted Star Pattern ---")
    for row in range(5):
        # Print leading spaces
        for col in range(row):
            print(" ", end="")
        # Print stars
        for star in range(5 - row):
            print("*", end=" ")
        print()  # Newline
    print()

    # 3. 5x5 Multiplication Table
    print("--- 3. 5x5 Multiplication Table ---")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i * j}", end="\t")
        print()  # Newline after each row


if __name__ == "__main__":
    demonstrate_nested_loops()
