questions=("1.What is the capital of india?",
          "2.Which animal lays the largest eggs?",
          "3.What is the hottest planet in the solar system?")
options=(("a.Chennai", "b.Dehli", "c.Andra" ,"d.Mumbai"),
         ("a.Whale", "b.Ostrich" ,"c.Anaconda", "d.Snake"),
         ("a.Venus","b.Mercury", "c.Mars", "d.Jupiter"))
answers=("b","b","a")
guesses=[]
que_num=0
score=0
for question in questions:
    print(question)
    for option in options[que_num]:
        print(option)
    guess = input("Enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess==answers[que_num]:
     score+=1
     print("Correct!")
    else:
     print("Incorrect!")
    print("The correct answer is:",[que_num])
    que_num+=1
