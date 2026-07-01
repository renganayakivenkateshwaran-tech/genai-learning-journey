principal=0
rate=0
time=0
principal =int( input("Enter the principal amount: "))
while principal <=0:
    print("principal can't be less than or equal to zero")
    principal =int( input("Enter the principal amount: "))
print(principal)

rate =int( input("Enter the rate of interest: "))
while rate <=0:
    print("rate can't be less than or equal to zero")
    rate =int( input("Enter the rate of interest: "))
print(rate)
time =int( input("Enter the time in years: "))
while time <=0:
    print("time can't be less than or equal to zero")
    time =int( input("Enter the time in years: "))
print(time)
total=principal*pow(1+rate/100,time)
print(total)
