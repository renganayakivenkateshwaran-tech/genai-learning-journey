# Membership operators are used to check whether a value or variable is present in a sequence (like a string, list, tuple, set, or dictionary).
#string
word="NAME"
letter = input("Enter a letter: ").upper()
if letter in word:
    print(f"{letter} is in the word" )
else:
    print(f"{letter} is not found")

#list
student = ["Tara","Banu","Chitra","Mathi"]
lists = input("Enter a student name: ").capitalize()
if lists in student:
    print(f"{lists} is a student")
else:
    print(f"{lists} was not found")

#tuple
food = ("Apple","Banana","Chicken","Mango")
lists = input("Enter a food name: ").capitalize()
if lists not in food:
    print(f"{lists} was not found")
else:
    print(f"{lists} is found")

#dictionary
students = {"Achu":90,
            "Bala":81,
            "Banu":71,
            "Vidhu":80}
stu = input ("Enter a student name: ").capitalize()
if stu in students:
    print(f"{stu} is a student Mark:{students[stu]}")
else:
    print(f"{stu} was not found")
