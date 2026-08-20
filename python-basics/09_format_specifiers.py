"""
Demonstration of String Format Specifiers in Python f-strings.

Specifiers Covered:
- Precision (.2f)
- Field Width & Padding (10, 010)
- Alignment (< left, > right, ^ center)
- Sign Flags (+)
- Thousands Separator (,)
"""

def Fixed_point_precision() -> None:
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31
    print("--- 1. Fixed-Point Precision (.2f) ---")
    print(f"price1: {price1:.2f}")
    print(f"price2: {price2:.2f}")
    print(f"price3: {price3:.2f}\n")

def width_padding() -> None:
    # 2. Width Padding (10 spaces total width)
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31
    print("--- 2. Spaces Width Padding (10) ---")
    print(f"price1: {price1:10}")
    print(f"price2: {price2:10}")
    print(f"price3: {price3:10}\n")
 
    # 3. Zero Padding (010 -> 10 total width padded with zeros)
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31
    print("--- 3. Zero Padding (010) ---")
    print(f"price1: {price1:010.2f}")
    print(f"price2: {price2:010.2f}")
    print(f"price3: {price3:010.2f}\n")

def alignment() -> None:
    # 4. Text Alignment (< Left, > Right, ^ Center with width 12)
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31
    print("--- 4. Alignment Specifiers ---")
    print(f"Left  : |{price1:<12.2f}|")
    print(f"Right : |{price1:>12.2f}|")
    print(f"Center: |{price1:^12.2f}|\n")

def sign_flag() -> None:
    # 5. Show Sign Flag (+)
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31
    print("--- 5. Explicit Sign (+) ---")
    print(f"price1: {price1:+.2f}")
    print(f"price2: {price2:+.2f}")
    print(f"price3: {price3:+.2f}\n")

def separator() -> None:
    # 6. Thousands Separator (,)
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31
    print("--- 6. Thousands Separator (,) ---")
    print(f"price1: {price1:,.2f}")
    print(f"price2: {price2:,.2f}")
    print(f"price3: {price3:,.2f}\n")

def combined() -> None:
    # 7. Combined Formatting (Sign + Separator + Width + Precision)
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31
    print("--- 7. Combined Example (+,12.2f) ---")
    print(f"price1: {price1:+,12.2f}")
    print(f"price2: {price2:+,12.2f}")
    print(f"price3: {price3:+,12.2f}")


if __name__ == "__main__":
    demonstrate_format_specifiers()
