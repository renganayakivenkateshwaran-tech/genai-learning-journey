#1
# if statements - if the if black is true the statement written on it will be executed. or the else block will be executed.

age  = int (input ("what's your age"))
if (age>=18):
              print ("you are eligible for voting")
else :
              print ("you are NOT eligible for voting")

#elif statement - If more than two conditions occurs we use elif        

#2
name  = (input ("what's your name?: "))
if(len(name) < 4) :
              print ("Too short")
elif ("." in name or "," in name):
              print ("Not valid") 
elif (len(name) > 15) :
              print ("Only 12 characters are allowed")
else:
    print ("Welcome!")

