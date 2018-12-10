"""
    1. 写出装饰器的模板格式
"""


def wrapper(func):
    def inner(*args, **kwargs):
        # 函数执行之前要做的事情
        ret = func(*args, **kwargs)
        # 函数执行之后要做的事情
        return ret

    return inner


@wrapper
def func1():
    print("hello")


# func1()

"""
# 2.编写装饰器，
    为多个函数加上认证的功能（用户的账号密码来源于文件），
    # 要求登录成功一次，后续的函数都无需再输入用户名和密码
"""

flag = False


def login(func):
    def inner(*args, **kwargs):
        global flag
        if flag:
            ret = func(*args, **kwargs)
            return ret
        else:
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            if username == "mike" and password == "123456":
                flag = True
                ret = func(*args, **kwargs)
                return ret

    return inner


@login
def shop_list():
    print("展示商品列表")


@login
def car_list():
    print("展示购物车列表")


shop_list()
car_list()
