#!/usr/bin/env python
# -*-coding:utf-8 -*-
import math
# ss = {'a': 'aaa','b':'bb'}
# print(ss['a'])
# names= ['michael','bob','tracy']
# scores = [95,75,85]
# ss['zhang']=100
# print(ss)
# print(ss.get('zhang1',-1))
# ss.pop('zhang')
# print(ss)
# print(hex(10000))
def my_abs(x):
    if isinstance(x,(float,int)):
        xx=float(x)
        if xx >= 0:
            return xx
        else:
            return -xx
    else:
        return "inputerror"

def nop():
    pass
def quadratgic(a,b,c):
    if b*b-4*a*c < 0:
        return "no result"
    elif b*b-4*a*c == 0:
        return (-b)/(2*a)
    else:
        x1=((-b)+math.sqrt(b*b-4*a*c))/(2*a)
        x2=((-b)-math.sqrt(b*b-4*a*c))/(2*a)
        return  x1,x2
def pow(x,n):
    s=1
    while n>0:
        s=s*x
        n=n-1
    while n<0:
        s=s/x
        n=n+1
    return s;
def enroll(name,gender,age=6,city='beijing'):
    print("name:",name)
    print("gender:",gender)
    print("age",age)
    print("city",city)
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n
    return sum
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
def triangles(max):
    n=1
    list1=[1]
    pass
class Students(object):
    pass


