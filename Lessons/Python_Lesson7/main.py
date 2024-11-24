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

#print(getTime())

class Dog:
    def __init__(self, name):
        self.name = name
        print(self)
    
    def bark(self):
        print('bark')

# obj = Dog('karl')
# obj = object()
#print(obj)

class Animal: 
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    breed: str

    def __init__(self):
        super().__init__("name")

    def bark(self):
        return "Waf Waf!"
    
    @staticmethod
    def static_function():
        print('static')
    
# my_dog = Dog("name")
# my_dog.bark()
# Dog.static_function()

class Cat:
    def meaow(self):
        self._make_sound()
    
    def _make_sound(self): # Protected
        pass

    def __private_method():
        pass

class WhiteCat(Cat):
    def meaow(self):
        return super().meaow()

class Dog:
    def __str__(self):
        return "this is a dog"
    
dog = Dog()
print(dog)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    
point1 = Point(1,2)
point2 = Point(2,3)
point3 = point1 + point2
print(point3)