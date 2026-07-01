temp = float(input("Enter the tempareture: "))
unit = input ("Enter the unit (F or c): ")
if unit == "F":
    temp = (temp * 9/5) + 32
    print ("Tempareture is",temp,"*C")
elif unit == "C":
    temp = (temp-32)*5/9
    print ("Tempareture is",temp,"*F")
else:
    print (f"{unit} is not vaild")
