# *args is used in a function definition to allow the function to accept any number of positional arguments.
#*args collects extra positional arguments into a tuple.
#The name args is just a convention — you can use any name, but the * is required.
#1
def add(*sums):
    total=0
    for sum in sums:
     total+=sum
    return total
print(add(9,2,3))
#2
def name(*args):
   for arg in args:
      print(arg,end=" ")
name("Achu","Bala","Yami","Kavi","Priya")
