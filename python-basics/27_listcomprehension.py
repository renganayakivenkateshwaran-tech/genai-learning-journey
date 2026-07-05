#List comprehension is a concise and readable way to create lists from existing iterables by applying an expression and optionally filtering elements.
#Syntax-[expression for value in range if condition]

#1
doubles = [x*2 for x in range(1,11)]
print(doubles)
five_table = [x*5 for x in range(1,11)]
print(five_table)