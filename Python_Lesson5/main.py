def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)
def p(v):
    print(v)
    return v
# print(factorial(2))
# a = 1
# print(p(a := a * 3) + p(a := a + 1))
# print(a)

arr: list = ['asdf','basdf']

import random

def getWord(words = (
    'мир',
    'пчелка',
    'самолет',
    'крендель',
    'кукушка',
    'тюрьма',
    'штраф',
    'мишфит',
    'рунамикон'
)):
    return random.choice(words)
    

def guesser(word:str):
    print(f'Угадайте слово из {len(word)} букв')
    print('Введите слово:')
    word = word.lower()
    v = ""
    while(word != (v := input().lower())):
        count = 0
        for i in v:
            if(i in word):
                count+=1
        print(f'угадано букв: {count}')
    print(f"Вы угадали слово! слово: {word}")

#guesser(getWord())


def guessNumber(): 
    n = random.randint(1,int(input("input lenght")))
    while(n != (v:= int(input('input any number:')))): 
        print('bigger' if n > v else 'lesser')
    else: print(f'You win! number: {n}')

# guessNumber()

# var: list[str] = ['sdf','asdf','v']

# import utils 
# print(utils.sum(1,1))
# from utils import sum
# print(sum(1,1))
# from utils import sum as utilsSum
# print(utilsSum(1,1))
# from .utils import sum, minus
# from . import utils
# from utils import *
# import utils
# import time
# from datetime import datetime
# now = datetime.now()
# print(now)
# from typing import List, Any

# import requests 
# response = requests.get("http://example.com")
# print(response.content)

# pip freeze
# py -m venv venv
# .\venv\Scripts\activate
# pip freeze > requirements.txt
# deactivate
# pip install -r .\requirements.txt

#import py_dir
#py_dir.module.someFunction()
# from py_dir import someFunction
# someFunction()

# a = {}
# try:
#     a['key']
#     1/0
#     raise Exception
# except (KeyError, ZeroDivisionError) as e: 
#     print(e)
# except Exception:
#     print('Exception')
# else:
#     print('else')
# finally: 
#     print('finally')

# sum_lambda = lambda a, b: a + b
# print(sum_lambda(1,2))

from typing import Callable

def my_callable_func(func: Callable):
    print(func())

my_callable_func(lambda: 'value')