"""
    一. 学习send()函数
        1. send()函数也可以获取下一个值
        2. send()函数可以给上一个yield的位置传递数据
        3. 第一次使用生成器的时候, 只能用next获取下一个值
           若第一次使用send()的话, 会报错: TypeError: can't send non-None value to a just-started generator
        4. 最后一个yield不能接收外部的值

    二. 生成器的应用
        1. 计算移动的平均值
        2. 预激生成器
            # 使用装饰器修饰生成器函数后, 可以让得到的生成器, 默认先执行一遍__next__()方法
            # 这样, 用户可以得到生成器后, 直接使用send()方法
"""


def generator():
    print(123)
    content = yield 1
    print('=======', content)
    print(456)
    arg = yield 2


# 调用生成器函数, 得到一个生成器
# g = generator()
# ret = g.__next__()
# print(ret)
# ret2 = g.__next__()
# print(ret2)

# 调用生成器函数, 得到一个生成器
g = generator()

# 第一次使用生成器的时候, 不能使用send()函数
# g.send(1)

# 输出: 123
ret1 = g.__next__()

# 输出: 1
print(ret1)

# 输出: ======= hello world
# 输出: 456
g.send("hello world")


# 2. 生产器的应用
# 计算移动的平均值
# 10 20 30 10
# 10 15 20 17.5
def get_average():
    sum = 0
    avg = 0
    count = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count


g = get_average()
g.__next__()
v1 = g.send(10)
print("平均速度为: ", v1)
v2 = g.send(20)
print("平均速度为: ", v2)


# 3. 预激生成器
def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()
        return g

    return inner


# 使用装饰器修饰生成器函数后, 可以让得到的生成器, 默认先执行一遍__next__()方法
# 这样, 用户可以得到生成器后, 直接使用send()方法
@init
def get_average2():
    sum = 0
    avg = 0
    count = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count


g2 = get_average2()
ret11 = g2.send(10)
print(ret11)

ret22 = g2.send(20)
print(ret22)
