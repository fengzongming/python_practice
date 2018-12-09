# 带一个参数的装饰器
import time


def timmer(f):
    def inner(name):
        start_time = time.time()
        ret = f(name)
        end_time = time.time()
        print("函数执行时间为:", end_time - start_time)
        return ret
    return inner


@timmer
def func(name):
    time.sleep(0.01)
    return name

res = func("hello")
print(res)