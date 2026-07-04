#1
'''
for y in range(0,2):
 for x in range(0,5):
  print(x,end=",")
  '''
#2
rows=5
for x in range(rows):
    for col in range(rows):
        print(" ",end=" ")
    for star in range (5-rows):
        print("*",end=" ")
    print()


