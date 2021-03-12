# Author: your name
# Date: 2021-02-09 14:41:03
# LastEditTime: 2021-02-09 15:10:30
# LastEditors: Please set LastEditors
# Description: 利用Request类创建请求
# FilePath: \PythonStudy\ScratchPY\use_basic_lib\urllib_use\lesson_2.py

from urllib import request,parse

url = 'https://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;windows NT)',
    'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req,timeout=100)
print(response.read().decode('utf-8'))