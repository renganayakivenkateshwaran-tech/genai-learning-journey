"""
Demonstrations of advanced concepts in function

Concepts covered
- Mulitiple return values
- Unpacking returned values
- Passing function as argument
- function returning function

"""

# Mulitiple return values -  A function can return multiple values by separating them with commas.They are returned as a tuple.

def get_details():
    name = "Alice"
    age = 20
    country = "America"
    return name,age,country
print(get_details())