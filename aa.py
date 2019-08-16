#!/usr/bin/env python
# -*- coding:utf-8 -*-
# input('输入用户\n')
# print("hello,world")
# age=input("age")
# if int(age)>18:
#     print("adult")
# else:
#     print("yor")
import bb
import math
import sys
#a=input()
# print(math.pi)
# a=bb.pow(3,-2)
# print(a)
# bb.enroll('sd','f',city='dats',age=5)
# print(bb.calc(2,3,4))
# alist=[1,2,3.4]
# print(bb.calc(*alist))
# n1='zhang'
# n2='jpe'
# print(n1+n2)
# bb.person('zha',20,city='bwj',jj='20')
#print(bb.fact(100))
# g=(x*x for x in range(10))
# for a in g:
#     print(a)
# gg=bb.fib(6)
# for a in gg:
#     print(a)
# args=sys.argv
# print(args)
# barft=bb.Students();
# print(barft)
import os
#print("Process (%s) start ..." % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print("i am child process (%s) and my parent is %s." %(os.getpid(),os.getppid()))
# else:
#     print("i (%s) just created a child process(%s)" %(os.getpid(),os.getppid()))
# import json
# d = {"name":"zhangjpe","age":20,"score":88}
# s = '{"name":"zhangjpe","age":20,"score":88}'
# b = json.loads(s)
# print(d)
# print(b)
# print(s)
import pickle
# d = dict(name='bob',age=20,score=88)
# print(pickle.dumps(d))
# f = open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()
# f = open("dump.txt",'rb')
# d = pickle.load(f)
# f.close()
# print(d)
# import json
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
# def student2dict(std):
#     return {
#         'name':std.name,
#         'age':std.age,
#         'score':std.score
#     }
# s = Student('zhaang',2,2)
# print(json.dumps(s,default=student2dict))
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print("run child process %s (%s)..." %(name,os.getpid()))
# if __name__=='__main__':
#     print('parent process %s' % os.getppid())
#     p = Process(target=run_proc,args=('test',))
#     print("child process will start.")
#     p.start()
#     p.join()
#     print('child process end')
# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print('run task %s (%s)...' % (name,os.getppid()))
#     start = time.time()
#     time.sleep(random.random())
#     end =time.time()
#     print('task %s run %0.2f seconds' %(name,(end-start)))
# if __name__=='__main__':
#     print("parent process %s" % os.getpid())
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('waiting for all subprcoess done...')
#     p.close()
#     p.join()
#     print('all subprocess done')
# import subprocess
# print('$nslookup www.baidu.com')
# r = subprocess.call(['nslookup','www.baidu.com'])
# print('exitcod',r)
# from multiprocessing import Process,Queue
# import os ,time ,random
# def write(q):
#     print("process to write :%s" % os.getpid())
#     for value in ['A','B','C']:
#         print('put %s to queue' %value)
#         q.put(value)
#         time.sleep(random.random())
# def read(q):
#     print('Process to read %s' % os.getpid())
#     while True:
#         value=q.get(True)
#         print('Get %s form queue' %value)
# if __name__=='__main__':
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.join()
#     pr.terminate()
import time,threading,multiprocessing
# def loop():
#     print('thread %s in running...' % threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s >>> %s ' %(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended' % threading.current_thread().name)
# print('thread %s is running'% threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
#
# print('thread %s ended' % threading.current_thread().name)
# balance = 0
# lock = threading.Lock()
# def chang_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for i in range(10000000):
#         lock.acquire()
#         try:
#             chang_it(n)
#         finally:
#             lock.release()
# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(3,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
# for  i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
local_school = threading.local()
def process_student():
    std = local_school.student
    print("hello, %s (in %s)" %(std,threading.current_thread().name))
def process_thread(name):
    local_school.student=name
    process_student()
t1 = threading.Thread(target=process_thread,args=('alice',),name="thread-A")
t2 = threading.Thread(target=process_thread,args=('bob',),name="thread-B")
t1.start()
t2.start()
t1.join()
t2.join()
