#List comprehension is a concise and readable way to create lists from existing iterables by applying an expression and optionally filtering elements.
#Syntax-[expression for value in range if condition]

#1
doubles = [x*2 for x in range(1,11)]
print(doubles)
five_table = [x*5 for x in range(1,11)]
print(five_table)

#2
numbers = [2,-5,-2,9,3,-8,0]
positive_num = [num for num in numbers if num>=0]
negative_num = [num for num in numbers if num<0]
print(negative_num)

#3
animals = ["dog","cat","bull","lion","tiger"]
capital=[animal.upper() for animal in animals]
Index_0=[animal[0] for animal in animals]
print(capital)

#4
marks =[90,78,45,74,29,32]
pass_mark = [mark for mark in marks if mark>=45]
print("PASS")
print(pass_mark)