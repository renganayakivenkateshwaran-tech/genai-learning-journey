temp = float(input("Enter the temperature: "))
unit = input ("Enter the unit (F or c): ")
if unit == "F":
    temp = (temp * 9/5) + 32
    print ("Temperature is",temp,"*C")
elif unit == "C":
    temp = (temp-32)*5/9
    print ("Temperature is",temp,"*F")
else:
    print (f"{unit} is not vaild")
