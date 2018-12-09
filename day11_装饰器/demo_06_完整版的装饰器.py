def wrapper(func):
    def inner(*args, **kwargs):
        # 函数执行前的操作
        res = func(*args, **kwargs)
        # 函数执行后的操作
        return res
    return inner
