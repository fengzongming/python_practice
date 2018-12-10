"""
    生成器函数:
        1. 只要含有yield关键字的函数都是生成器函数
        2. 生成器函数执行之后会得到一个生成器作为返回值

"""


def generator():
    print(1)
    yield 'a'
    yield 'b'
    yield 'c'


ret = generator()
print(ret.__next__())
print(ret.__next__())
print(ret.__next__())
