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



#3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Division by zero is not allowed")
    case _:
        print("Invalid operator")
