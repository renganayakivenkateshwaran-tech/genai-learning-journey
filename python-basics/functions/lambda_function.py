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