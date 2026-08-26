"""
Demonstration of recursion in python.

Concept covered
- Recursion structure
- Base case
- Recursive case
- Example programs
"""

"""
Recursion is when a function calls itself directly or indirectly to solve a problem by breaking it into smaller subproblems.
A recursive function must have:
- Base Case  -  Stops the recursion.
- Recursive Case  - Calls itself with a smaller/simpler input.
"""
# sum of n numbers

def add(n):
    if n==0:
        return 0          # Base case
    return n + add(n-1)   # Recursive case
print(add(7))

# Count up

def count(n):
    if n>10:
        return       # Base case
    print(n)
    return count(n+1)   # Recursive case
print(count(1))

# string reversing

def rev(s):
    if s == "":
        return " "
    return s[-1] + rev(s[:-1])
print(rev("snake"))

# factorial

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))


