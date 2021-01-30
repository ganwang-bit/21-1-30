# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """

# from time import time
# def is_differ(a: str,b,c) ->bool:
#     li = []
#     for i in a:
#         if eval(i) not in li:
#             li.append(eval(i))
#         else:
#             continue
#     for i in b:
#         if eval(i) not in li:
#             li.append(eval(i))
#         else:
#             continue
#     for i in c:
#         if eval(i) not in li:
#             li.append(eval(i))
#         else:
#             continue
#     if len(li) == 9:
#         return True
#     else:
#         return False
# start = time()
# #a = [i for i in range(150,350)]
# #b = [i for i in range(350,660)]
# #c = [i for i in range(550,999)]
# a = (i for i in range(150,350))
# b = (i for i in range(350,660))
# c = (i for i in range(550,990))
# for i in a:
#     for j in b:
#         for k in c:#is_differ判断三个数字是否完全相异 123 456 789
#             # print(i,j,k)
#             if i*2 == j and i*3 == k and int(j*1.5) == k and is_differ(str(i), str(j), str(k)):
#                 print(i,j,k)
# print(time()-start)
# import time
# def showtim(func):
#     def swaper():
#         start=time.time()
#         func()
#         end=time.time()
#         print(start-end)
#     return swaper
# @showtim #p=showtime(p)
# def p():
#     print("yes")
# p()
# import time
# from functools import wraps
# def showtime(func):
#     @wraps(func)
#     def wapper():
#         start=time.time()
#         func()
#         end=time.time()
#         print("spend time is {}".format(start-end))
#     return wapper
# @showtime 
# def func():
#     print("func...")
#     for i in range(100):
#         print(i)
# func()
# print(func.__name__)
# import time
# class Fun(object):
#     def __init__(self,func):
#         self._func=func
#     def __call__(self):
#         start_time=time.time()
#         self._func()
#         end_time=time.time()
#         print("spend time is {}".format(start_time-end_time))
# @Fun
# def func():
#     for i in range(100):
#         print(i)
#     time.sleep(1)
# func()
# print(func.__name__)
# a=[1,2,3,4]
# b=a
# a[0]=4
# print(b)
# print(a)
# 中=1
# print(中)
# a=[1,2,3,4]
# print(range(10))
# a=[1,2,3]
# if not isinstance(a,int):
#     raise TypeError ("Type Error")
# s=input()
# while ' ' in s:
#     if s[0]==' ':
#             s=s[1:]
#     if s[len(s)-1]==' ':
#         s=s[:len(s)]
# print(s)
# def trim(s):
#     while ' ' in s:
#         if s[0]==' ':
#             s=s[1:]
#         if s[len(s)-1]==' ':
#             s=s[:len(s)-1]
#     return s
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')
# a=10
# if(isinstance(a,int )):
#     print("int")
# [str(i)+str(j) for i in range(1,9) for j in range(1,9)]
    # n=0
    # a=[1,1]
    # b=[]
    # while True:
    #     count=0
    #     if n==0:
    #         yield [1]
    #         n+=1
    #     if n==1:
    #         yield [1,1]
    #         n+=1
    #     b.append(1)
    #     while count+1<len(a):
    #         b.append(a[count]+a[count+1])
    #         count+=1
    #     b.append(1)
    #     a=b
    #     b=[]
    #     yield a
# from functools import reduce
# def f(x,y):
#     return 10*x+y
# def l(i):
#     temp={str(i):i for i in range(1,10)}
#     return temp[i]
# print(reduce(f,map(l,"123456789")))
# a=(i for i in range(1,10))
# print(list(a))
# def pan(i):
#     return i%2
# a=filter(pan,[1,2,3,4,5,6,7,8,9])
# print(list(a))
# def shengcheng():
#     n=2
#     while True:
#         yield n
#         n=n+1
# def l(x):
#     def pan(n):
#         return n%x
#     return pan
# def sushu():
#     lie=shengcheng()
#     while True:
#         n=next(lie)
#         yield n
#         lie=filter(l(n),lie)
# for i in sushu():
#     print(i)
#     if i>100:
#         break
# def is_palindrome(n):
#     a=list(str(n))
#     b=a.copy()
#     b.reverse()
#     return a==b
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# import time
# def showtime(func):
#     def swpper():
#         start=time.time()
#         func()
#         end=time.time()
#         print("spend time is {}",(start-end))
#     return swpper
# def creat(r,g,b):
#     while True:
#         R='R'*r
#         G='G'*g
#         B='B'*b
#         RGB=R+G+B
#         i=0
#         tmp=[]
#         while i<len(RGB)-2:
            
    














