"""
Object oriented programming - Way of writing programs by organizing code around objects.
Class - Blueprint to create objects.
Objects -  Actual thing created from that blueprint.
An object represents:
Data - What the object has.
Behaviour - What the object can do.
A class contains:
Method - A function inside a class.
Attributes - Data that belong to an object.
"""

class Car:
    def __init__(self,color,model,year):
        self.color = color
        self.model = model
        self.year  = year          # color,model,year are the attributes (data).
    def start(self):
        print(f"Starting the {self.model}")
    def stop(self):
        print(f"Stopping the {self.model}")
    def info(self):
        print(f"Color: {self.color}\nModel:  {self.model}")     # start,stop,info are the methods(behaviour).
car1 = Car("white","mustang",2026)     # Creating object
car2 = Car("Black","Tesla",2025)     # Another object
car1.start()     # accessing the method
car2.stop()
car1.info()
car2.info()