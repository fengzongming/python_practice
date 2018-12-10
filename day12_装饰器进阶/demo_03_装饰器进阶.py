"""
    带参数的装饰器:
        通过给装饰器传参数, 来控制是否需要执行装饰器的作用
"""
import time

flag = True


def time_out(flag):
    def timmer(func):
        def inner(*args, **kwargs):
            if flag:
                start_time = time.time()
                ret = func(*args, **kwargs)
                end_time = time.time()
                print("函数执行的时间: ", end_time - start_time)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret

        return inner

    return timmer


# @time_out(False)
@time_out(True)
def func1():
    time.sleep(0.01)
    print("hello func1")


# func1()

"""
    多个装饰器装饰同一个函数
        wrapper1, wrapper2, wrapper3装饰func2
"""


def wrapper1(func):
    def inner1():
        print('wrapper1 ,before func')
        ret = func()
        print('wrapper1 ,after func')
        return ret

    return inner1


def wrapper2(func):
    def inner2():
        print('wrapper2 ,before func')
        ret = func()
        print('wrapper2 ,after func')
        return ret

    return inner2


def wrapper3(func):
    def inner3():
        print('wrapper3 ,before func')
        ret = func()
        print('wrapper3 ,after func')
        return ret

    return inner3


@wrapper1
@wrapper2
@wrapper3
def func2():
    print("hello func2")


"""
    执行结果(简单记忆为俄罗斯套娃):
        wrapper1 ,before func
        wrapper2 ,before func
        wrapper3 ,before func
        hello func2
        wrapper3 ,after func
        wrapper2 ,after func
        wrapper1 ,after func
"""
func2()
