'''
Author: your name
Date: 2021-02-09 15:15:36
LastEditTime: 2021-02-22 17:49:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PythonStudy\ScratchPY\use_basic_lib\urllib_use\lesson_4.py
'''

# Author: your name
# Date: 2021-02-09 15:15:36
# LastEditTime: 2021-02-09 15:21:06
# LastEditors: Please set LastEditors
# Description: In User Settings Edit
# FilePath: \PythonStudy\ScratchPY\use_basic_lib\urllib_use\lesson_4.py


from urllib.error import URLError
from urllib.request import build_opener,ProxyHandler

proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com',timeout=100)
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
