# print('hello world')
import typing
# isinstance([1,2,3,4], list)

# def func1(i: int, b: list):
#     """
#     this function accepts list
#     """
#     return i

#numbers = [1,2,3,4]
# print(numbers.index(3))

#filter1 = filter(lambda x: x % 2 == 0, numbers)
#print(list(filter1))
#import re

# regex = r'^abc$'
# email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}'
 
# email = 'yelemanov.temirlan@gmail.com'
# if re.match(email_regex, email):
#     print('correct')
# else:
#     print('incorrect')

# text = "I am here"
# new_text = re.sub(r'am', 'was', text)
# print(new_text)

#re.findall

# file = open('file.txt', 'w')
# file = open('file.txt', 'a')
#file = open('file.txt', 'r')
#lines = ['asdf', 'asdfbdfad']
#file.writelines(lines)
#file.write('hello world')
# content = file.read()
# for line in file:
#     print(line.strip())

# while(line:= file.read()):
#     print(line)
# file.close()

# with open('my_file.txt','r') as file:
#     for line in file.readlines():
#         print(line)

# import os

# if os.path.exists('file.txt'):
#     print('it exists')

# print(f'Размер файл {os.stat("file.txt")} байт')
# os.rename('file.txt', 'file.txt')

# os.mkdir('my_new_dir')

# def countUpToTen():
#     count = 1
#     while count <= 10:
#         yield count
#         count += 1

# counter = countUpToTen()
# for i in counter:
#     print(i)

def func2():
    yield 'value1'
    yield 'value2'
    yield 'value3'
    
# for i in func2():
#     print(i)

def func3():
    v = 0
    while(True):
        yield (v := v+1)

if True:
    pass


def decorator1(func):
    def wrapper(*args, **kwrgs):
        result = func(*args, **kwrgs)
        return result * 2
    return wrapper

@decorator1
@decorator1
def add(arg1, arg2):
    return arg1 + arg2

# dec = decorator1(add)
# print(dec(1,2))

# print(add(1,2))

def dec2(mult: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * mult
        return wrapper
    return decorator1


def func3(v1, v2):
    pass