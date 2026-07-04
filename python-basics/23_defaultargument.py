#parameters that have a predefined value in a function definition.
#If the caller does not provide a value for that parameter, Python uses the default.
#1
'''
def net_price(list_price,discount=0.5,tax=0.01):
    return list_price*(1-discount)*(1+tax)
print(net_price(500))
print(net_price(500,0.4))
'''
#2
import time
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    return(start,end)
count(10)
