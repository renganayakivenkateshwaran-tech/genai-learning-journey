"""
Demonstration of **kwargs (Arbitrary Keyword Arguments) in Python.

Concepts Covered:
- Accepting a dynamic number of key=value (keyword) arguments
- Packing keyword arguments into a Dictionary
- Iterating over key-value pairs using .items()
- Formatted output for key alignment
"""

from typing import Any


# 1. Printing Student Information using **kwargs
def print_student_info(**kwargs: Any) -> None:
    for key, value in kwargs.items():
        print(f"{key:8}: {value}")


# 2. Combining Regular Arguments with **kwargs
def create_profile(username: str, **attributes: Any) -> None:
    print(f"User Profile for: @{username}")
    for key, value in attributes.items():
        print(f" - {key}: {value}")


def demonstrate_kwargs() -> None:
    # Example 1: Student Details
    print("--- 1. Student Record (**kwargs) ---")
    print_student_info(
        Name="Achu",
        Mark=90,
        Grade="A+",
        Rollno="027"
    )
    print()

    # Example 2: Flexible User Profile Creation
    print("--- 2. Flexible Profile Creation ---")
    create_profile(
        "ren_tech",
        role="Developer",
        language="Python",
        experience_years=2,
        is_active=True
    )


if __name__ == "__main__":
    demonstrate_kwargs()
