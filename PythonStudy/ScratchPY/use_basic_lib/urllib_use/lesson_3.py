'''
Author: your name
Date: 2021-02-09 13:43:35
LastEditTime: 2021-02-09 15:06:12
LastEditors: Please set LastEditors
Description: 利用Handler请求需要验证的网站
FilePath: \PythonStudy\Study\scrach_from_browser\scratch_when_need_passward.py
'''


from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = input('请输入需要验证的网站：')

p = HTTPPasswordMgrWithDefaultRealm()#HTTPPasswordMgrWithDefaultRealm()类将创建一个密码管理对象，用来保存 HTTP 请求相关的用户名和密码
p.add_password(None,url,username,password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url,timeout=100)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)