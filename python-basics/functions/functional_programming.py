"""
Demonstration of functional programming.

Concept Covered 
- map()
- filter()
- soretd()
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
