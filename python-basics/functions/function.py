"""
Demonstration of functions in python

Concepts covered:
- Function parameter and arguments
- Return statement
- Scope & Variable (Local variable,Global variable,Global keyword)
"""

#Function structure
def basic_func():      # def keyword creates a function
    return("Hello,This is the demonstration of function!")
result=basic_func()
print(result)

"""
Parameters and arguments
Parameter - A parameter is a variable defined in the function declaration (inside the parentheses) that
        acts as a placeholder for the value the function will receive.
Argument - An argument is the actual value you pass to the function when calling it.

"""
def parameter(x,y):   #x,y are the parameters
    return x+y
result=parameter(4,5) #4,5 are the arguments of the parameters
print(result)

"""
Return statement - The return statement is used inside a function to send a value (or multiple values) back to the caller.

"""
def return_demo(a,b,c,d):  
    return a+b-c*d
result=return_demo(4,5,2,4) 
print(result)

"""
Scope - Scope defines where a variable is accessible in your code.

"""
# Local variable - A variable created inside a function

def greet():
    name="Alice"
    print (f"Hello! {name}")
greet()

# Global variable - A variable created outside all functions.

greet = "Hello"

def greeting(name):
    print(greet,name)
greeting("Tom")

# Global keyword - If we want to make changes in global variable we use global keyword.

num = 5

def add():
    global num
    return num+5
print(add())

 



     