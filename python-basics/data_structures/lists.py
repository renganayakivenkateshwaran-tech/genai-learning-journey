"""
Demonstration of Python Lists and List Methods.

Characteristics:
- Ordered, mutable collection
- Allows duplicate elements
- Supports indexing, slicing, and built-in methods
"""

    students = ["Sam", "Balu", "Deepika", "Atchaya"]
    marks = [56, 85, 90, 93]
    
def inspection_membership() -> None:
    # 1. Inspection & Membership
    print("--- 1. Inspection & Membership ---")
    print(f"List length: {len(students)}")
    print(f"Is 'Sam' in students? {'Sam' in students}\n")

def index_slice() -> None:
    # 2. Indexing & Slicing
    print("--- 2. Indexing & Slicing ---")
    print(f"First student [0]: {students[0]}")
    print(f"Slice [0:4]: {students[0:4]}")
    print(f"Reversed slice [::-1]: {students[::-1]}\n")

def append_insert() -> None:
    # 3. Adding Elements (append, insert)
    print("--- 3. Adding Elements ---")
    students.append("Kayal")
    print(f"After append('Kayal'): {students}")

    students.insert(0, "Sana")
    print(f"After insert(0, 'Sana'): {students}\n")

def search_count() -> None:
    # 4. Searching & Counting
    print("--- 4. Searching & Counting ---")
    print(f"Count of 'Sam': {students.count('Sam')}")
    print(f"Index of 'Balu': {students.index('Balu')}\n")

def remove() -> None:
    # 5. Removing Elements (remove, pop)
    print("--- 5. Removing Elements ---")
    students.remove("Balu")
    print(f"After remove('Balu'): {students}")

def pop() -> None:
    popped_element: str = students.pop()
    print(f"Popped element: '{popped_element}'")
    print(f"After pop(): {students}\n")

def sort() -> None:
    # 6. Sorting & Reversing (In-Place)
    print("--- 6. Sorting & Reversing ---")
    students.sort()
    print(f"Sorted alphabetically: {students}")

def reverse() -> None:
    students.reverse()
    print(f"Reversed order: {students}\n")

def Concatenation_Reoetition() -> None:
    # 7. List Operations (Concatenation & Repetition)
    print("--- 7. Operations ---")
    combined: list[str | int] = marks + students
    print(f"Concatenation (marks + students): {combined}")
    print(f"Repetition (marks * 3): {marks * 3}\n")

def clearing() -> None:
    # 8. Clearing a List
    print("--- 8. Clearing List ---")
    students.clear()
    print(f"After clear(): {students}")


if __name__ == "__main__":
    remove()
