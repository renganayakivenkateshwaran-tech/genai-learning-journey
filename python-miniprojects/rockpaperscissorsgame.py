import random
options=("Rock","Paper","Scissor")
while True:
    player=None
    computer=random.choice(options)
    while player not in options:
     player = input("Enter a choice (Rock,paper,Scissors): ").capitalize()
    print(f"Player:{player}")
    print(f"Computer:{computer}")
    if player==computer:
     print("TIE!")
    elif player == "Paper" and computer=="Rock":
     print("You Win!")
    elif player == "Rock" and computer=="Scissors":
     print("You Win!")
    elif player == "Scissors" and computer=="Paper":
     print("You Win!")
    else:
     print("You Lose!")
    play_again=input("Press (y) to play again: ")
    if not play_again == "y":
     break