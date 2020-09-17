
import time
import random

def sleep(n_secs):
    time.sleep(n_secs)


#python所有函数的定义只能在debugtalk.py中定义
def get_user_agent():
    user_agent=["danshui1","danshui2","danshui3","danshui4"]
    return random.choice(user_agent)

def get_accounts():
    #要返回一个嵌套字典的列表（数据来源于数据库等）
    accounts=[
        {"title":"正常登录", "username": "keyou1", "password": "123456",
            "status_code": 200, "contain_msg": "token"},
        {"title":"账号错误", "username": "keyou1111", "password": "123456",
            "status_code": 400, "contain_msg": "non_field_errors"},
        {"title":"密码错误", "username": "keyou1", "password": "123457",
            "status_code": 400, "contain_msg": "non_field_errors"},
        {"title": "账号为空", "username": "", "password": "123456",
         "status_code": 400, "contain_msg": "username"},
        {"title": "密码为空", "username": "keyou1", "password": "",
         "status_code": 400, "contain_msg": "password"}
    ]
    return accounts

if __name__ == '__main__':
    print(get_user_agent())
