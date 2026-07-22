"""
Demonstration of Logical Operators in Python.

Operators Covered:
- and : Returns True if ALL conditions are True
- or  : Returns True if AT LEAST ONE condition is True
- not : Reverses the boolean state (True -> False, False -> True)
"""


def demonstrate_logical_operators() -> None:
    a: int = 4
    b: int = 9
    c: int = 17

    # 1. Logical AND
    print("--- Logical AND ---")
    and_result: bool = (a < 8) and (b == 9) and (c < 20)
    print(f"Condition (a < 8 and b == 9 and c < 20): {and_result}")

    # Practical AND Example: Authentication (Requires BOTH admin status AND correct password)
    is_admin: bool = True
    original_password: str = "ABCERT"
    entered_password: str = input("Enter password for AND test: ")

    if is_admin and original_password == entered_password:
        print("Access Allowed (Both conditions met)\n")
    else:
        print("Access Denied\n")

    # 2. Logical OR
    print("--- Logical OR ---")
    or_result: bool = (a == b) or (b == 9) or (c > 10)
    print(f"Condition (a == b or b == 9 or c > 10): {or_result}")

    # Practical OR Example: Guest or Admin Access (Requires EITHER condition)
    if is_admin or original_password == entered_password:
        print("Access Allowed (At least one condition met)\n")
    else:
        print("Access Denied\n")

    # 3. Logical NOT
    print("--- Logical NOT ---")
    is_logged_in: bool = False
    print(f"Original Status: {is_logged_in}")
    print(f"Negated Status (not is_logged_in): {not is_logged_in}")


if __name__ == "__main__":
    demonstrate_logical_operators()
