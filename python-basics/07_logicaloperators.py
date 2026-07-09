# Logical operators are used to perform specific task on a variable or values. it will return either True or False value.

#Logical and- All the condition must be true in order to return True value.
#1
a=5
b=9
c=12
print(a>0 and b==9 and c<20)
#2
Is_admin = True 
original_Password = "ABCERT"
Entered_password = input ("Enter the password: ")
if (Is_admin and original_Password==Entered_password ):
    print ("Access Allowed")
else:
    print ("Access Denied")
      
#Logical or - At least one condition must be true.
#1
print (a==b or b==9 or c > 10)  #Even if the first condition is false it will check the second condition.
#2
Is_admin = True 
original_Password = "ABCERT"
Entered_password = input ("Enter the password: ")
if (Is_admin or original_Password==Entered_password ):
    print ("Access Allowed")
else:
    print ("Access Denied")

#Logical not - Reverse the condition (not true == false, not false = true).
#1
print(not(a)) #Only returns True if a=0 ,0-False, not False-->True














