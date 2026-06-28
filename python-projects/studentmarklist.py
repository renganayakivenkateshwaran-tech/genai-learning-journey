students=[]
marks=[]
total=0
average=0
while True:
    stu=input("\nEnter the name: ")
    if stu.lower() == "q":
        break
    else:
        students.append(stu)
        mark = float(input ("Enter the mark: "))
        marks.append(mark)
        total+=mark
    for stu in students:
        print(stu,end="   ")
    print()
    for mark in marks:
        print(mark,end="   ")
print("The total is: ",total)
average=total/len(marks)
print("The average is: ",average)

        