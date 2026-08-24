"""
Demonstration of lambda functions in python.

Concepts Covered
- Lambda syntax
- Lambda with map()
- Lambda with filter()
- Lambda with sorted()
- Lambda with dictionaries
- Lambda with max and min
- Lambda with reduce 

"""

# Lambda - A lambda function is a small, anonymous function defined using the lambda keyword.

# Lambda syntax - Lambda arguments : Expression.
res = lambda x:x*3
print(res(2))

# Lambda with map() 
# map() - map() takes the function and apply to every element.

numbers = [1,2,3,4,5]

res = list(map(lambda num:num*2,numbers))
print(res)

# Lambda with filter()
# filter() - keep only the items that satisty a condition.

numbers = [1,2,3,4,5,6,7,8,9,10]

res = list(filter(lambda num : num % 5 == 0,numbers))
print(res)

# Lambda with sorted()
# sorted() - sorts the elements in ascending order.

students = [("Alice",98),
            ("Bob",76),
            ("Charlie",82),
            ("Dara",94)]
# Sorting by marks
res = sorted(students,key=lambda stu:stu[0])
print(res)

# Sorting by names
res = sorted(students,key=lambda stu:stu[1])
print(res)