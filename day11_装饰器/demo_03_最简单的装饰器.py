"""
    装饰器类型:
        1. 最简单的装饰器
        2. 有返回值的装饰器
        3. 有一个参数的装饰器
        4. 万能参数的装饰器

    装饰器作用:
        在不修改函数源码的情况下, 给函数增加功能

    语法糖: @
"""

import time


def timmer(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print("函数执行时间为:", end_time - start_time)

    return inner


@timmer
def func():
    time.sleep(0.01)
    print("hello 装饰器")


# func = timmer(func)
func()
