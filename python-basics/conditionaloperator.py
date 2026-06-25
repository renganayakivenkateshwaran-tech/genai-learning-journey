# Conditional Operator is used as the shortcut of if statements.
# SYNTAX--> X if condition else Y
a=3
b=5
#1
print (a if a>b else b)
#2
print ("EVEN" if a%2==0 else "ODD")
#3
user = "admin"
print("Full Access" if user=="admin" else "Limited access")
#4
name = "USER7675"
password = "123!!!09879"
print("Welcome!",name if password == "123!!!09879" else "Incorrect password! Try Again.")