# 带返回值的装饰器
import time


def timmer(f):
    def inner():
        start_time = time.time()
        ret = f()
        end_time = time.time()
        print("程序执行时间为", end_time - start_time)
        return ret

    return inner


@timmer
def func():
    time.sleep(0.01)
    return "hello everybody"


res = func()
print(res)
