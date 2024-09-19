# set1 = {1,2,3,4,5,6}
# set2 = {9,10,20,1,2}
# set1.add(7)
# set1.remove(6)
# print(set1)
# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# print(set1 + set2) # will not work

# dict = {"key 1": "value 1", "key 2": "value 2"}
# print(dict["key 1"])
# del dict["key 1"]
# print(dict)
# print(dict.keys)
# print(list(dict.keys()))
# dictkeys = dict.keys()
# print(list(dict.values()))
# print(list(dict.items()))

# my_list = [1,2,3,4]
# for i in my_list:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(3,10,2):
#     print(i)

# for i in range(0, len(my_list),2):
#     print(my_list[i])

# testtuple = {1,"Hello"}
# a,b = testtuple

# print(a)
# print(b)


# arr = [1,2,'stop', 3]
# for i in arr:
#     if i == 'stop':
#         break
#     print(i)
# else:
#     print("end of cycle")


# while i:=1 < 10:
#     i+=1
#     if i%2 == 0:
#         continue
#     print(i)
# else:
#     print("end of while cycle")

# x = 10
# if(x>5):
#     print("yep")
# elif x==5:
#     print('5')
# else:
#     print('no')

# a = [1,2]
# b = [1,2]
# a == b
# a is b
# a = 0
# while a <10: print(a:=a+1)
# if a == 10: print('yes'), print(10)

# c = a if a == 10 else 'no'
# print(c)
# def func1():
#     print('hello')

# def func2():
#     return func1

# func2()()

# def func(arg1: int) -> int:
#     return 'hello'

# print(func(1.24))

# def func(a, *args: int):
#     for arg in args:
#         print(arg)

# func(1,2,3,4,5)

# def func(**kwargs):
#     for key, value in kwargs.items():
#         print(key," ", value)

# def func(arg1, *args: int, **kwargs: str):
#     pass

# func(arg1=1, )

# def func() -> function:
#     def funct():
#         print('hello')
#     return funct

# func()()