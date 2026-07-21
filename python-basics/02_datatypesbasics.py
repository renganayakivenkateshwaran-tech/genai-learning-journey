"""
Demonstration of core Python primitive data types: int, float, str, and bool.
"""

def demonstrate_datatypes() -> None:
    # 1. Integers (int)
    age: int = 18
    language_count: int = 5

    # 2. Floating-Point Numbers (float)
    gpa: float = 8.0
    average: float = 90.5

    print(f"I'm {age} years old, my GPA is {gpa}, and I speak {language_count} languages.")
    print(f"My average score is {average}.")

    # 3. Strings (str)
    name: str = "Renga Nayaki"
    print(f"Name: {name}")

    # 4. Booleans (bool) - using snake_case naming
    is_for_sale: bool = True
    status: str = "Available" if is_for_sale else "Not Available"
    print(f"Item Status: {status}")


if __name__ == "__main__":
    demonstrate_datatypes()
