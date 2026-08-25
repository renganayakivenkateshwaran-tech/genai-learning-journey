"""
Demonstration of functional programming.

Concept Covered 
- map()
- filter()
- sorted()
- reduce()
- zip
- any()
- all()
"""

#map() - map() applies a function to every item in an iterable.
numbers = [1,2,3,4,5,6,7,8]

res = list(map(lambda num : num + num , numbers))
print(res)

#filter() - filter() function extracts elements from an iterable that satisfy a specific condition.
numbers = [1,2,,3,7,9,5,3]

res = list(filter(lambda num : num % 2 == 0,numbers))
print(res)

#sorted() - returns a new sorted list from the elements of any iterable object.
employees = [{"name":"Kavitha","emp_no":10},
             {"name":"Achu","emp_no":02},
             {"name":"Deepika","emp_no":17},
             {"name":"Pooja","emp_no":28},
             {"name":"kayal","emp_no":05}]
res = sorted(employees,key = lambda employee : employee ["emp_no"])
print(res)
            
#reduce() - shrink" or collapse a collection of data into one result.
from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]

res = reduce(lambda x,y : x+y, numbers)
print(res)

# any() - a built-in tool that returns True if at least one element in an iterable evalutes to true.
numbers = [1,2,3,4,5,6,7,8,9,10]

res = any(num > 5 for num in numbers)
print(res)

# all() - returns True if every single item in a collection is true. If even one item is false.
numbers = [1,2,3,4,5,6,7,8,9,10]

res = all(num > 5 for num in numbers)
print(res)


