#The match…case statement, enables structural pattern matching, allowing cleaner and more expressive conditional logic compared to long if-elif-else chains.
def day_of_week(day):
    match day:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
         case 3:
            print("Tuesday")   
        
