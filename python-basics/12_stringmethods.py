
"""
Demonstration of built-in Python string methods.
String methods use dot (.) notation and return new values.
"""

name = input("Enter your name: ")

# len() is a built-in function, not a method, but crucial for strings
print(f"Length of name: {len(name)}")

# Case conversions
print(f"Capitalized: {name.capitalize()}")
print(f"Upper case: {name.upper()}")
print(f"Lower case: {name.lower()}")
print(f"Title case: {name.title()}")

# Basic checks (returns True/False)
print(f"Is alphabetic only?: {name.isalpha()}")
print(f"Is it a decimal number?: {name.isdecimal()}")
print(f"Is alphanumeric?: {name.isalnum()}")
print(f"Starts with 'Hello'?: {name.startswith('Hello')}")
print(f"Ends with 'world'?: {name.endswith('world')}")

# Searching and manipulating
print(f"Index of first space: {name.find(' ')}")
print(f"Index of last 'd': {name.rfind('d')}")
print(f"Count of letter 'a': {name.count('a')}")

# Modifications
print(f"Replacing dashes with spaces: {name.replace('-', ' ')}")
print(f"Stripped whitespace: '{name.strip()}'")
print(f"Split into a list: {name.split()}")
