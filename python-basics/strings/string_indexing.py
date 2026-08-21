"""
Demonstration of String Indexing and Slicing in Python.

Syntax:
    string[start : end : step]

Concepts Covered:
- Positive & Negative Indexing
- Slicing Range [start:end]
- Step Slicing [::step] & String Reversal [::-1]
- Handling IndexError safely
"""


def demonstrate_string_indexing() -> None:
    phone_number: str = "7364-37847-49834"

    # 1. Single Character Indexing
    print("--- 1. Single Character Indexing ---")
    print(f"First character [0]: {phone_number[0]}")
    print(f"Last character [-1]: {phone_number[-1]}\n")

    # 2. String Slicing [start:end]
    print("--- 2. Range Slicing ---")
    print(f"First 5 characters [0:5]: {phone_number[0:5]}")
    print(f"Middle slice [5:9]: {phone_number[5:9]}")
    print(f"Last 5 characters [-5:]: {phone_number[-5:]}\n")

    # 3. Step Slicing & Reversal
    print("--- 3. Step Slicing & Reversal ---")
    print(f"Every 2nd character [::2]: {phone_number[::2]}")
    print(f"Reversed string [::-1]: {phone_number[::-1]}\n")

    # 4. Practical Example: Masked Phone Number
    print("--- 4. Practical Example ---")
    last_4_digits: str = phone_number[-4:]
    print(f"Masked Phone Number: XXXX-XXXX-{last_4_digits}\n")

    # 5. Out of Bounds Index Handling
    print("--- 5. IndexError Handling ---")
    try:
        invalid_char: str = phone_number[50]
        print(invalid_char)
    except IndexError:
        print("Error: Index 50 is out of range for this string.")


if __name__ == "__main__":
    demonstrate_string_indexing()
