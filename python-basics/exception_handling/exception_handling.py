"""
A comprehensive guide to Exception Handling in Python.
Covers try, except, else, finally blocks, and raising custom errors.
"""

# =====================================================================
# 1. Understanding the Exception Handling Flow
# =====================================================================
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block executes code when NO exceptions occur.
# The finally block executes code REGARDLESS of the outcome.

def divide_numbers(numerator, denominator):
    try:
        print(f"\n--- Attempting division: {numerator} / {denominator} ---")
        result = numerator / denominator
        
    except ZeroDivisionError as e:
        # Runs ONLY if a ZeroDivisionError occurs
        print(f"Caught an Error: Cannot divide by zero! ({e})")
        
    except TypeError as e:
        # Runs ONLY if data types are wrong (e.g., dividing a string by a number)
        print(f"Caught a Type Error: Please provide numbers only. ({e})")
        
    else:
        # Runs ONLY if the try block succeeded without any errors
        print(f"Success! The result is: {result}")
        
    finally:
        # ALWAYS runs, perfect for cleanup actions (closing files, databases, etc.)
        print("Division cleanup: This block always executes.")

# Testing the different pathways:
divide_numbers(10, 2)    # Triggers: try -> else -> finally
divide_numbers(10, 0)    # Triggers: try -> except ZeroDivisionError -> finally
divide_numbers(10, "2")  # Triggers: try -> except TypeError -> finally


# =====================================================================
# 2. Raising Exceptions Manually (The 'raise' keyword)
# =====================================================================
# You can deliberately force an exception to occur if business logic fails.

def validate_age(age):
    print(f"\n--- Validating age: {age} ---")
    
    if not isinstance(age, int):
        raise TypeError("Age must be a whole number integer.")
        
    if age < 0:
        # Raising a built-in ValueError with a custom message
        raise ValueError("Age cannot be negative!")
        
    if age < 18:
        print("Access Denied: You must be 18 or older.")
    else:
        print("Access Granted: Welcome!")

# Handling raised exceptions cleanly
try:
    validate_age(-5)
except ValueError as error:
    print(f"Validation Failed: {error}")

try:
    validate_age("eighteen")
except TypeError as error:
    print(f"Validation Failed: {error}")

