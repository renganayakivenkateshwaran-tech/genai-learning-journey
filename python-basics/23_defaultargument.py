"""
Demonstration of Default Arguments in Python Functions.

Concepts Covered:
- Assigning predefined default values to parameters
- Positional argument overriding (supplying 1, 2, or all arguments)
- Combining default parameters with range/time operations
"""

import time


# 1. Price Calculation with Default Discount and Tax
def calculate_net_price(list_price: float, discount: float = 0.5, tax: float = 0.01) -> float:
    return list_price * (1 - discount) * (1 + tax)


# 2. Counter Function with Default Start Value
def count(end: int, start: int = 0) -> tuple[int, int]:
    print(f"Counting from {start} to {end}:")
    for x in range(start, end + 1):
        print(x)
        time.sleep(0.1)  # Brief delay for smooth execution
    return start, end


def demonstrate_default_arguments() -> None:
    # Example 1: Net Price Calculations
    print("--- 1. Net Price with Default Parameters ---")
    
    # Uses default discount (0.5) and default tax (0.01)
    price_default = calculate_net_price(500)
    print(f"Default Discount & Tax (500): {price_default:.2f}")

    # Overrides discount to 0.4, uses default tax (0.01)
    price_custom_discount = calculate_net_price(500, 0.4)
    print(f"Custom Discount 0.4 (500, 0.4): {price_custom_discount:.2f}")

    # Overrides both discount (0.2) and tax (0.05)
    price_custom_all = calculate_net_price(500, 0.2, 0.05)
    print(f"Custom Discount & Tax (500, 0.2, 0.05): {price_custom_all:.2f}\n")

    # Example 2: Range Counter
    print("--- 2. Counter with Default Start Value ---")
    
    # Uses default start (0)
    range_info = count(5)
    print(f"Returned Range Tuple: {range_info}\n")

    # Overrides start value to 2
    count(5, start=2)


if __name__ == "__main__":
    demonstrate_default_arguments()
