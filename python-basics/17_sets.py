"""
Demonstration of Python Sets and Set Operations.

Characteristics:
- Unordered collection (no index-based access)
- Unique elements only (automatically removes duplicates)
- Mutable (supports adding and removing elements)
"""


def demonstrate_sets() -> None:
    stu1_mark: set[int] = {90, 82, 91, 72, 66}
    stu2_mark: set[int] = {72, 89, 92, 74, 62}

    print("--- Initial Sets ---")
    print(f"Student 1 Marks: {stu1_mark}")
    print(f"Student 2 Marks: {stu2_mark}\n")

    # 1. Modifying Sets (add, remove)
    print("--- 1. Modifying Sets ---")
    stu1_mark.add(99)
    print(f"After add(99): {stu1_mark}")

    stu1_mark.remove(90)  # Note: Raises KeyError if element is missing; use discard() for safe removal
    print(f"After remove(90): {stu1_mark}\n")

    # 2. Mathematical Set Operations
    print("--- 2. Mathematical Operations ---")
    
    # Union (|) : All unique elements from both sets
    print(f"Union (stu1 | stu2): {stu1_mark | stu2_mark}")

    # Intersection (&) : Elements present in BOTH sets
    print(f"Intersection (stu1 & stu2): {stu1_mark & stu2_mark}")

    # Difference (-) : Elements in stu1 but NOT in stu2
    print(f"Difference (stu1 - stu2): {stu1_mark - stu2_mark}")

    # Symmetric Difference (^) : Elements in EITHER set, but NOT in BOTH
    print(f"Symmetric Difference (stu1 ^ stu2): {stu1_mark ^ stu2_mark}")


if __name__ == "__main__":
    demonstrate_sets()
