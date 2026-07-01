import random
lowest_value=1
highest_value=20
answer=random.randint(lowest_value,highest_value)
guesses_count=0
print("Python Number Guessing Game")
print("---------------------------")
print(f"Pick a number between {lowest_value} and {highest_value}")
while True:
    guess=input("Enter a number: ")
    if guess.isdigit():
        guess=int(guess)
        guesses_count+=1
    else:
         print("Invalid")
         continue
    if guess==answer:
            print("Correct")
            guess=int(guess)
            print("The correct answer is: ",answer)
            break
    elif guess>20 or guess<1:
         print("Out of range")
    elif guess<answer:
         print("Too low! Try again")
    elif guess>answer:
         print("Too high! Try a;gain")
    
print("Guesses: ",guesses_count)
