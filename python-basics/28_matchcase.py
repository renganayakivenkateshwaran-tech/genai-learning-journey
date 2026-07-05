#The match…case statement, enables structural pattern matching, allowing cleaner and more expressive conditional logic compared to long if-elif-else chains.
def day_of_week(day):
    match day:
        case 1:
            return("Sunday")
        case 2:
            return("Monday")
        case 3:
            return("Tuesday")
        case 4:
            return("Wednesday")
        case 5:
            return("Thursday")
        case 6:
            return("Friday")
        case 7:
            return("Saturday")
        case _:
            return("Not valid")

print(day_of_week(5))
           
#2
def Is_weekend(day):
    match day:
        case "Sunday"|"Saturday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thrusday"|"Friday":
            return False
        case _:
            return("Not valid")

print(Is_weekend("Sunday"))
        
