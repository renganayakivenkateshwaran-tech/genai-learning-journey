"""
Demonstration of Keyword Arguments in Python Functions.

Concepts Covered:
- Passing arguments using parameter names (name=value)
- Argument order independence
- Improved code readability and self-documentation
"""


# 1. Greeting Generator
def greet(greeting: str, title: str, first: str, last: str) -> None:
    print(f"{greeting}, {title}. {first} {last}!")


# 2. Phone Number Formatter
def format_phone_number(country: int | str, area: int | str, first: int | str, last: int | str) -> None:
    print(f"+{country} ({area}) {first}-{last}")


def demonstrate_keyword_arguments() -> None:
    # 1. Keyword Arguments in Order
    print("--- 1. Keyword Arguments (Standard Order) ---")
    greet(greeting="Hello", title="Mr", first="John", last="Doe")

    # Demonstrating Order-Independence (Passing arguments out of order)
    print("\n--- Out-of-Order Example ---")
    greet(last="Doe", greeting="Good Morning", first="Jane", title="Ms")

    # 2. Phone Number Example with Keyword Arguments
    print("\n--- 2. Phone Number Formatter ---")
    format_phone_number(country=91, area=10, first=14671, last=88962)


if __name__ == "__main__":
    demonstrate_keyword_arguments()
