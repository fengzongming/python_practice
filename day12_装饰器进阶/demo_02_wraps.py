from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """inner函数的注释"""
        print("函数执行之前要完成的操作")
        ret = func(*args, **kwargs)
        print("函数执行之后要完成的操作")
        return ret

    return inner


def func1(day):
    """这是一个放假通知"""
    print('全体放假%s天' % day)
    return '好开心'


@wrapper
def func2(day):
    """这是一个上班通知"""
    print('全体上班%s天' % day)
    return '好开心'


print(func1.__name__)
print(func1.__doc__)

# 原函数被装饰器的语法糖装饰后, 打印函数的函数名__name__和函数的注释__doc__,
# 打印的是inner函数的函数名和inner函数的注释
# 如果我们想要打印被装饰器装饰后的函数, 原函数名和函数的注释的话, 需要使用@wraps(函数名)装饰inner函数
print(func2.__name__)
print(func2.__doc__)
