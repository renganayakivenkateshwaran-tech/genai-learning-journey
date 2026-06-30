menu = {"pizza":2.3,
        "burger":3.5,
        "nachos":4.1,
        "popcorn":6.4}
cart=[]
total=0
for key,value in menu.items():
    print(f"{key:8}:{value:.2f}")
while True:
    food = input ("Enter the foods you like: (press q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food,end="")
print(f"Your total is ${total:.2f}")