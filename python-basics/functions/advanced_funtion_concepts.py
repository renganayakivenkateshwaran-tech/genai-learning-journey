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

# Unpacking returned values - A function can return multiple values by packing them into a tuple (or other iterable), and you can unpack them directly into variables.

def get_details():
    name = "Alice"
    age = 20
    country = "America"
    return name,age,country
name,age,country = get_details()
print(name)
print(age)
print(country)

"""
 Passing function as argument - Functions are first-class objects, meaning you can pass them as arguments to other functions,
            return them from functions, and store them in variables or data structures.
"""

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def calculate(operation,x,y):
    return operation(x,y)
print(calculate(add,15,10))
