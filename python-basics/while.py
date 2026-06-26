#1
'''
num=0
while num<=10:
    print(num)
    num=num+1
'''
#2
'''
num=1
while num<=10:
    print(f"3x{num}={num*3}")
    num=num+1
'''
#3 
'''
password="python123"
user_pwd=input("Enter the password: ")

while not user_pwd == "python123":
    print("Incorrect password!")
    user_pwd=input("Enter the correct password: ")

print("Welcome!")
'''
#4
age=int(input("Enter your age: "))
while age<18 or age>100:
    print("Too old or Too young")
    age=int(input("Enter your correct age: "))
print("Welcome to our website!")

