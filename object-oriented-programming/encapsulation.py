"""
Deomstration of encapsulation.

Concepts Covered:
- Public attributes.
- Protected attributes.
- Private attributes.
- Name mangling
- @property
- Getter
- Setter
"""
"""
Encapsulation -  The practice of binding data and methods into a single class and restricting direct access to some attributes 
                                        to protect the internal state of an object.
"""
# Public attributes - Can be accessed directly from outside the class.
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
student1 = Student("Ani",18)
print(student1.name)
print(student1.age)

# Protected attributes - Is a class member (variable or method) whose name starts with a single underscore (_).
class Employee:
    def __init__(self,name,id_no,salary):
        self.name = name
        self.id_no = id_no
        self._salary = salary
    def show_salary(self):
        print(self._salary)
employee = Employee("Akilan",101,50000)
employee.show_salary()

# Private attributes - Indicates that an attribute is intended to be private using double underscore.
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def show_balance(self):
        print("Balance:",self.__balance)
account1 = BankAccount(100000)
account1.show_balance()

# Name mangling - Used to make class attributes less accessible from outside the class and to avoid accidental name conflicts, especially in inheritance.
class Code:
    def __init__(self):
        self.__code = "apple123"
obj = Code()
print(obj._Code__code)

# @property Makes mathods behave like attributes.

class Add:
    def __init__(self,num):
        self.__num = num
    @property
    def addition(self):
        return self.__num + 90
num1 = Add(10)
print(num1.addition)
