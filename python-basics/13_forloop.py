"""
Demonstration of Loops and Loop Control Statements in Python.

Concepts Covered:
- time.sleep(): Delays execution by specified seconds
- reversed(): Reverses sequence iteration
- continue: Skips current iteration
- break: Exits loop prematurely
- String Iteration: Looping through individual characters in a string
"""

import time


def demonstrate_loops() -> None:
    # 1. Basic Loop with Delay (Counting Up)
    print("--- 1. Sleep Function (Count Up) ---")
    for x in range(0, 3):  # Reduced range to 3 for faster demonstration
        print(x)
        time.sleep(0.5)
    print()

    # 2. Reverse Loop with Delay (Countdown)
    print("--- 2. Reversed Function (Countdown) ---")
    for x in reversed(range(0, 4)):
        print(x)
        time.sleep(0.5)
    print()

    # 3. Continue Keyword (Skips number 9)
    print("--- 3. Loop with Continue (Skip 9) ---")
    for x in reversed(range(7, 11)):
        if x == 9:
            continue  # Skip 9 and move to next iteration
        print(x)
    print()

    # 4. Break Keyword (Stops loop at 9)
    print("--- 4. Loop with Break (Stop at 9) ---")
    for x in reversed(range(7, 11)):
        if x == 9:
            break  # Exit loop completely
        print(x)
    print()

    # 5. String Iteration
    print("--- 5. String Range Iteration ---")
    credit_num: str = "7472-8362-9872"
    for char in credit_num:
        print(char)


if __name__ == "__main__":
    demonstrate_loops()
