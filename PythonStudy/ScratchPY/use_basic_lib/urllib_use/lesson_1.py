'''
Author: your name
Date: 2021-02-06 09:33:33
LastEditTime: 2021-02-09 14:54:30
LastEditors: Please set LastEditors
Description: 利用urllib库发送请求的基本测试代码（利用parse、request、error模块&socket库）
FilePath: \PythonStudy\ScratchPY\use_basic_lib\urllib_use\lesson_1.py
'''


#urlopen时最好带着timeout参数，否则会被网站认证为攻击

import socket
import urllib.parse
import urllib.request
import urllib.error


#1、GET请求抓取
response = urllib.request.urlopen('https://www.python.org',timeout=100)

#打印测试
print("\n网页类型：")
print(type(response))
print("\n网页源代码如下：")
print(response.read().decode('utf-8'))
print("\n响应的状态码（200-Yes 404-No）：")
print(response.status)
print("\n响应头：")
print(response.getheaders())
print("\n响应头中Server值：")
print(response.getheader('Server'))
print()


#2、POST方式请求抓取

#bytes-字节串，以字节序列的形式（二进制形式）来存储数据，特别适合用于网络数据传输
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print("\n请求信息：")
print(response.read())
print()

# response = urllib.request.urlopen('https://httpbin.org/get',timeout=0.1)
# print(response.read())

#超时测试代码
try:
    response = urllib.request.urlopen('https://www.python.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')





