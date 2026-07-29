"""
Demonstration of match...case (Structural Pattern Matching) in Python.

Concepts Covered:
- Basic value matching & default wildcard case (_)
- OR pattern matching using the pipe (|) operator
- Guard conditions within case statements
"""


# 1. Day of Week Mapping
def day_of_week(day: int) -> str:
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Not valid"


# 2. Weekend Check using OR (|) Operator
def is_weekend(day: str) -> bool | str:
    match day.strip().capitalize():
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Not valid"


# 3. Interactive Calculator with Pattern Matching & Guards
def run_calculator() -> None:
    print("--- 3. Structural Pattern Matching Calculator ---")
    try:
        a: int = int(input("Enter first number: "))
        b: int = int(input("Enter second number: "))
        op: str = input("Enter operator (+, -, *, /): ").strip()

        match op:
            case "+":
                print(f"Result: {a + b}")
            case "-":
                print(f"Result: {a - b}")
            case "*":
                print(f"Result: {a * b}")
            case "/" if b != 0:  # Match guard for non-zero division
                print(f"Result: {a / b}")
            case "/":
                print("Error: Division by zero is not allowed.")
            case _:
                print("Error: Invalid operator.")
    except ValueError:
        print("Error: Please enter valid integers for numbers.")


def demonstrate_match_case() -> None:
    # Example 1
    print("--- 1. Day of Week ---")
    print(f"Day 5: {day_of_week(5)}")
    print(f"Day 9: {day_of_week(9)}\n")

    # Example 2
    print("--- 2. Weekend Check ---")
    print(f"Is 'Sunday' a weekend? {is_weekend('Sunday')}")
    print(f"Is 'Monday' a weekend? {is_weekend('Monday')}")
    print(f"Is 'Holiday' a weekend? {is_weekend('Holiday')}\n")

    # Example 3
    run_calculator()


if __name__ == "__main__":
    demonstrate_match_case()
