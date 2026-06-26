import time
my_time=int(input("Enter the time in seconds: "))
for x in reversed(range(0,my_time)):
    sec=x%60
    min=int(x/60)%60
    hour=int(x/3600)
    print(f"{hour}:{min}:{sec}")
    time.sleep(1)
