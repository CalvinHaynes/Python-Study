"""对用户名的存储和交互"""

import json

filename = 'D:/PYTHON/Study/Chapter_10/Example/username.json'

def get_stored_username():
    """得到已储存的用户名"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """得到新注册用户名"""
    new_username = input('please input your name:')
    with open(filename,'w') as f:
        json.dump(new_username,f)
    return new_username


def users_greet():
    """和注册用户打招呼的交互程序"""
    username = get_stored_username()
    if username:
        print(f"Hello,{username}")
    else:
        username = get_new_username()
        print(f"Now you have signed in our system,{username}")
        


users_greet()
