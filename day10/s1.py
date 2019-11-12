#!/usr/bin/env python
# -*- coding:utf-8 -*-
# shang = 9 // 2
# # yu = 9 % 2
# # name = '傻逼'
# # cc = 2**4
# # print(shang,yu,cc)
# # if '傻' in name:
# #     print('ok')
# # else:
# #     print('error')
# #
# # a1 = 123
# # v1 = a1.bit_length()
# # name1 = 'shizhengwen'
# # print(name1.upper())
# # num = "111"
# # v = int (num,base=2)
# # # print(v)
# for i in range(10):
#     print(i.bit_length())
# 格式化
import socket
sk=socket.socket()
sk.connect(('10.8.72.6',8801))

while True:
    inp=input(">>>>")
    sk.sendall(bytes(inp,"utf8"))
    data=sk.recv(1024)
    print(str(data,'utf8'))
