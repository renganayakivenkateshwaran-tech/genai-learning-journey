#keyword arguments- arguments passed to a function by their parameter name.
#1
def greet(greeting,title,first,last):
    print(f"{greeting}, {title} {first} {last}!")
greet(greeting="Hello",title="Mr",first="John",last="doe")
#2
def phone_num(country,area,first,last):
    print(f"{country}-{area}-{first}-{last}")
phone_num(country=91,area=10,first=14671,last=88962)