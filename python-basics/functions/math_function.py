"""
Demonstration of Python Built-in Math Functions and the 'math' Module.

Concepts Covered:
- Built-in functions: round(), abs(), min(), max()
- Standard library 'math' module functions: ceil(), floor(), sqrt(), pow()
- Mathematical constants: pi, e, tau, inf, nan
"""

import math


def demonstrate_math_functions() -> None:
    x: float = 4.65
    y: int = 8
    z: int = 9

    # 1. Built-in Math Functions
    print("--- 1. Built-in Math Functions ---")
    print(f"round({x}): {round(x)}")
    print(f"abs({x}): {abs(x)}")
    print(f"min({x}, {y}, {z}): {min(x, y, z)}")
    print(f"max({x}, {y}, {z}): {max(x, y, z)}\n")

    # 2. Math Module Functions
    print("--- 2. Standard Library 'math' Module ---")
    print(f"math.ceil({x}): {math.ceil(x)}")
    print(f"math.floor({x}): {math.floor(x)}")
    print(f"math.sqrt({x}): {round(math.sqrt(x), 2)}")
    print(f"math.pow({x}, {y}): {round(math.pow(x, y), 2)}\n")

    # 3. Mathematical Constants
    print("--- 3. Mathematical Constants ---")
    print(f"math.pi : {math.pi}")
    print(f"math.e  : {math.e}")
    print(f"math.tau: {math.tau}")
    print(f"math.inf: {math.inf}")
    print(f"math.nan: {math.nan}")


if __name__ == "__main__":
    demonstrate_math_functions()
