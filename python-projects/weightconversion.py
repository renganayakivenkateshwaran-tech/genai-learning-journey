weight = float(input ("Enter your weight: "))
unit =(input("Enter the unit of measurement (k/l): "))
if unit == "k":
        weight = weight * 2.205
        unit = "Lbs"
        print ("Your weight is",weight,unit)
elif unit == "l":
        weight = weight / 2.205
        unit = "kgs"
        print ("Your weight is",weight,unit)
else:
        print("Enter the correct unit of measurement")

