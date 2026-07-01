
# if statements - if the if black is true the statement written on it will be executed. or the else block will be executed.

age  = int (input ("what's your age"))
if (age>=18):
              print ("you are eligible for voting")
else :
              print ("you are NOT eligible for voting")

#elif statement - If more than two conditions occurs we use elif        


age  = int (input ("what's your age? "))
if(age<0) :
              print ("You haven't been born yet")
elif (age>=18):
              print ("you are eligible for voting") 
else:
              print ("you are NOT eligible for voting")

