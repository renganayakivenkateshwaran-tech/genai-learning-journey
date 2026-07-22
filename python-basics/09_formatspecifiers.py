"""
Demonstration of String Format Specifiers in Python f-strings.

Specifiers Covered:
- Precision (.2f)
- Field Width & Padding (10, 010)
- Alignment (< left, > right, ^ center)
- Sign Flags (+)
- Thousands Separator (,)
"""


def demonstrate_format_specifiers() -> None:
    price1: float = 6764.336
    price2: float = -983.489
    price3: float = 78677.31

    # 1. Fixed-point Precision (.2f)
    print("--- 1. Fixed-Point Precision (.2f) ---")
    print(f"price1: {price1:.2f}")
    print(f"price2: {price2:.2f}")
    print(f"price3: {price3:.2f}\n")

    # 2. Width Padding (10 spaces total width)
    print("--- 2. Spaces Width Padding (10) ---")
    print(f"price1: {price1:10}")
    print(f"price2: {price2:10}")
    print(f"price3: {price3:10}\n")

    # 3. Zero Padding (010 -> 10 total width padded with zeros)
    print("--- 3. Zero Padding (010) ---")
    print(f"price1: {price1:010.2f}")
    print(f"price2: {price2:010.2f}")
    print(f"price3: {price3:010.2f}\n")

    # 4. Text Alignment (< Left, > Right, ^ Center with width 12)
    print("--- 4. Alignment Specifiers ---")
    print(f"Left  : |{price1:<12.2f}|")
    print(f"Right : |{price1:>12.2f}|")
    print(f"Center: |{price1:^12.2f}|\n")

    # 5. Show Sign Flag (+)
    print("--- 5. Explicit Sign (+) ---")
    print(f"price1: {price1:+.2f}")
    print(f"price2: {price2:+.2f}")
    print(f"price3: {price3:+.2f}\n")

    # 6. Thousands Separator (,)
    print("--- 6. Thousands Separator (,) ---")
    print(f"price1: {price1:,.2f}")
    print(f"price2: {price2:,.2f}")
    print(f"price3: {price3:,.2f}\n")

    # 7. Combined Formatting (Sign + Separator + Width + Precision)
    print("--- 7. Combined Example (+,12.2f) ---")
    print(f"price1: {price1:+,12.2f}")
    print(f"price2: {price2:+,12.2f}")
    print(f"price3: {price3:+,12.2f}")


if __name__ == "__main__":
    demonstrate_format_specifiers()
