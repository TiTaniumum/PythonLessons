
class Class1:
    def __call__(self, arg1, arg2):
        return arg1 + arg2
    
# my_callable = Class1()
# print(my_callable(1,2))

# для статического метода self не нужен

from abc import ABC, abstractmethod
from typing import Any

class MyIteratorInterface(ABC):
    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __next__(self):
        ...
    
class MyListIterator(MyIteratorInterface):
    def __init__(self, collection: list) -> None:
        self.collection = collection

    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current < len(self.collection):
            result = self.collection[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

my_list = MyListIterator([1, 2, 3, 4])

# iterator = my_list.__iter__()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in my_list:
#     print(i)

class FibonacciGenerator:
    def __init__(self):
        self.a, self.b = 0,1

    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value
    
# fib = FibonacciGenerator()

# for _ in range(10):
#     print(next(fib))


class Animal:
    def sound(self):
        print("i made a sound")

class Flying: 
    def fly(self):
        print('i fly')

class Bird(Animal, Flying):
    ...

# bird = Bird()
# bird.fly()
# bird.sound()

class Parent1: 
    def greet(self):
        print("hello")

class Parent2:
    def greet(self):
        print("hello2")

class Child(Parent1, Parent2):
    def greet(self):
        super().greet()
        print("hello child")
    ...

# child = Child()
# print(child.greet())

#MRO - method resolution order
# ромбовидное наследование

# print(Child.__mro__[0]().greet())

# print(child.__class__.__mro__)

# class A:
#     pass

# class B(A):
#     pass
    
# class C(A):
#     pass

# class D(B,C):
#     pass

# print(D.mro())
#D - B - C - A


# class A:
#     pass 

# class B(A):
#     pass

# class C:
#     pass

# class D(B,C):
#     pass

# print(D.mro())
#D - B - A - C

class Class3:
    class_var = 0

    @classmethod
    def increment_class_var(cls):
        cls.class_var+=1



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Product: {self.name}, Price: {self.price}, Quantity {self.quantity}"
    
    def __add__(self, other: 'Product'):
        self.quantity + other.quantity
        try: 
            if self.name == other.name:
                return Product(self.name, self.price, self.quantity + other.quantity)
            else:
                raise TypeError
        except AttributeError:
            raise TypeError
        
    def __eq__(self, other) -> bool:
        return self.name == other.name
    

class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, warranty_id: int):
        super().__init__(name, price, quantity)
        self.warranty_id = warranty_id

class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date: str):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date


# product1 = FoodProduct("Apple", 2, 5,"11.10")
# product2 = FoodProduct("Banana", 2, 3, "11.10")
# product3 = FoodProduct("Apple", 2, 3, "11.10")

# try:
#     products = product1 + product2
# except TypeError:
#     print("type error")

# products = product3 + product1

# print(products)
# print(product3 == product1)

class Person:
    fio: str
    birthDate: str
    phone: str
    city: str
    country: str
    adress: str

    def __init__(self, 
                 fio, 
                 birthDate, 
                 phone, 
                 city, 
                 country,
                 adress):
        self.fio = fio
        self.birthDate = birthDate
        self.phone = phone
        self.city = city
        self.country = country
        self.adress = adress
        
    def __getitem__(self, name):
        if name == 'fio': return self.fio
        elif name == 'birthDate': return self.birthDate
        elif name == 'phone': return self.phone
        elif name == 'city': return self.city
        elif name == 'country': return self.country
        elif name == 'adress': return self.adress
        else: return None

    def __setitem__(self, name, value):
        if name == 'fio': self.fio = value
        elif name == 'birthDate': self.birthDate = value
        elif name == 'phone': self.phone = value
        elif name == 'city': self.city = value
        elif name == 'country': self.country = value
        elif name == 'adress': self.adress = value

class Fraction:
    numerator: int
    denomenator: int

    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.denomenator = denomenator
    
    def __str__(self) -> str:
        return f'{self.numerator}/{self.denomenator}'
    
    def __add__(self,other:'Fraction'):
        if(self.denomenator != other.denomenator):
            return Fraction(self.numerator * other.denomenator + self.denomenator * other.numerator, self.denomenator * other.denomenator)
        else:
            return Fraction(self.numerator + other.numerator, self.denomenator)
        
    def __sub__(self,other: 'Fraction'):
        if(self.denomenator != other.denomenator):
            return Fraction(self.numerator * other.denomenator - self.denomenator * other.numerator, self.denomenator * other.denomenator)
        else:
            return Fraction(self.numerator - other.numerator, self.denomenator)
        
    def __mul__(self, other: 'Fraction'):
        return Fraction(self.numerator * other.numerator, self.denomenator * other.denomenator)
    
    def __truediv__(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denomenator, self.denomenator * other.numerator)

a = Fraction(1,2)
b = Fraction(2,3)

print(a + b)
print(a - b)
print(a * b)
print(a / b)