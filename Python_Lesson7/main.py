def getEven(left, right):
    (left, right) = (right, left) if right < left else (left, right)
    count = left if left%2==0 else left+1
    while(count < right):
        yield count
        count+=2

#print(list(getEven(20,10)))

def sub(arr, start, end):
    (start, end) = (end, start) if end < start else (start, end)
    i = start
    while(i < end):
        yield arr[i]
        i+=1

print(list(sub([0,1,2,3,4,5,6,7,8], 6, 3)))

def CheckNumber(n, func):
    return func(n)

#print(CheckNumber(4, lambda x: x%2==0))

import time

def decorator_getTime(func):
    def wrapper():
        string = func()
        return string[11:16]
    return wrapper

def decorator_pretier(func):
    def wrapper():
        string = func()
        return "======================\n" + string + "\n======================"
    return wrapper

@decorator_pretier
@decorator_getTime
def getTime():
    return time.ctime()

print(getTime())

