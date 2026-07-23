"""
Demonstration of Python Lists and List Methods.

Characteristics:
- Ordered, mutable collection
- Allows duplicate elements
- Supports indexing, slicing, and built-in methods
"""


def demonstrate_lists() -> None:
    students: list[str] = ["Sam", "Balu", "Deepika", "Atchaya"]
    marks: list[int] = [56, 85, 90, 93]

    # 1. Inspection & Membership
    print("--- 1. Inspection & Membership ---")
    print(f"List length: {len(students)}")
    print(f"Is 'Sam' in students? {'Sam' in students}\n")

    # 2. Indexing & Slicing
    print("--- 2. Indexing & Slicing ---")
    print(f"First student [0]: {students[0]}")
    print(f"Slice [0:4]: {students[0:4]}")
    print(f"Reversed slice [::-1]: {students[::-1]}\n")

    # 3. Adding Elements (append, insert)
    print("--- 3. Adding Elements ---")
    students.append("Kayal")
    print(f"After append('Kayal'): {students}")

    students.insert(0, "Sana")
    print(f"After insert(0, 'Sana'): {students}\n")

    # 4. Searching & Counting
    print("--- 4. Searching & Counting ---")
    print(f"Count of 'Sam': {students.count('Sam')}")
    print(f"Index of 'Balu': {students.index('Balu')}\n")

    # 5. Removing Elements (remove, pop)
    print("--- 5. Removing Elements ---")
    students.remove("Balu")
    print(f"After remove('Balu'): {students}")

    popped_element: str = students.pop()
    print(f"Popped element: '{popped_element}'")
    print(f"After pop(): {students}\n")

    # 6. Sorting & Reversing (In-Place)
    print("--- 6. Sorting & Reversing ---")
    students.sort()
    print(f"Sorted alphabetically: {students}")

    students.reverse()
    print(f"Reversed order: {students}\n")

    # 7. List Operations (Concatenation & Repetition)
    print("--- 7. Operations ---")
    combined: list[str | int] = marks + students
    print(f"Concatenation (marks + students): {combined}")
    print(f"Repetition (marks * 3): {marks * 3}\n")

    # 8. Clearing a List
    print("--- 8. Clearing List ---")
    students.clear()
    print(f"After clear(): {students}")


if __name__ == "__main__":
    demonstrate_lists()
