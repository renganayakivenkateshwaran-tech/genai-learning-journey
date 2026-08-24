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

# Lambda with dictionary
department = [{"name":"IT","dept_no":10,"no_of_students":45},
              {"name":"DS","dept_no":9,"no_of_students":43},
              {"name":"CS","dept_no":11,"no_of_students":46},
              {"name":"AI","dept_no":8,"no_of_students":42}]
res = sorted(department,key=lambda dept:dept["no_of_students"])
print(res)

# Lambda with max and min
# max - finds the maximum value
students = [("Alice",98),
            ("Bob",76),
            ("Charlie",82),
            ("Dara",94),
            ("Xavier",99)]
res = max(students,key=lambda x : x[1])
print(res)

# min - finds the minimum value
students = [("Alice",98),
            ("Bob",76),
            ("Charlie",82),
            ("Dara",94),
            ("Xavier",99)]
res = min(students,key=lambda x : x[1])
print(res)