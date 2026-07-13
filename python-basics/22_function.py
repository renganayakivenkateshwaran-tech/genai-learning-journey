"""
A comprehensive guide to Python functions.
Covers definition, arguments, return values, scopes, and lambda functions.
"""

# =====================================================================
# 1. Defining Functions, Parameters, Arguments, & Return Values
# =====================================================================

# 'name' is a parameter (placeholder)
def greet_user(name):
    """Greets a user by their name."""
    return f"Hello, {name}! Welcome."  # return value sends data back


# "Achu" is the argument (the actual value passed)
greeting = greet_user("Achu")
print(greeting)


# =====================================================================
# 2. Default & Keyword Arguments
# =====================================================================

# 'msg' has a default argument. If not provided, it defaults to "Good morning"
def send_message(user, msg="Good morning"):
    print(f"{user}: {msg}")


send_message("Renga")  # Uses default argument
send_message("Renga", "Good night")  # Overrides default argument

# Using Keyword Arguments (ordering doesn't matter when named)
send_message(msg="How are you?", user="Vijay")


# =====================================================================
# 3. Variable-Length Arguments (*args and **kwargs)
# =====================================================================

def sum_all_numbers(*args):
    """*args collects extra positional arguments into a TUPLE."""
    print(f"args received: {args}")
    return sum(args)


print(f"Total Sum: {sum_all_numbers(10, 20, 30, 40)}")


def user_profile(**kwargs):
    """**kwargs collects extra keyword arguments into a DICTIONARY."""
    print(f"kwargs received: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")


user_profile(username="renga_tech", role="AI Developer", location="India")


# =====================================================================
# 4. Scope (Local vs. Global)
# =====================================================================

global_var = "I am global"  # Accessible anywhere in the file


def scope_demo():
    local_var = "I am local"  # Only accessible inside this function
    print(local_var)
    print(global_var)  # Functions can read global variables


scope_demo()
# print(local_var)  # <-- This would throw a NameError if uncommented!


# =====================================================================
# 5. Lambda Functions (Anonymous Functions)
# =====================================================================
# Syntax: lambda parameters: expression

# Regular function way:
# def square(x): return x * x

# Lambda way (concise, single-line functions):
square = lambda x: x * x
add_numbers = lambda a, b: a + b

print(f"Square of 5: {square(5)}")
print(f"Sum of 5 + 10: {add_numbers(5, 10)}")
