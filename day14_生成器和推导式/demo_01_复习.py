"""
    迭代器:
        双下方法: 很少直接调用, 一般情况下, 是通过其他语法触发

        可迭代的--可迭代协议:
            含有__iter__()方法
        迭代器--迭代器协议:
            含有__iter__()和__next__()方法

        可迭代的和迭代器之间的关系:
            1. 迭代器一定是可迭代的
            2. 可迭代的对象, 通过iter()方法, 可以得到一个迭代器

        迭代器的特点:
            1. 很方便使用, 但只能取所有的数据取一次
            2. 节省内存空间


    生成器:
         本质: 生成器本质就是迭代器

         表现形式:
            1. 生成器函数
            2. 生成器表达式

         生成器函数:
            含有yield关键的函数, 就是生成器函数

        特点:
            1. 调用函数之后, 函数不执行, 返回一个生成器
            2. 每次调用next()方法的后, 会取到一个值
            3. 直到取完最后一个, 再执行next()会报错

"""

# r1是一个可迭代的
r1 = range(10)

# 输出range(0, 10)
print(r1)

# 返回True
print("__iter__" in dir(r1))

# 返回False, 说明r1只是一个可迭代的, 不是迭代器
print("__next__" in dir(r1))

# 调用iter()方法, 把可迭代的 --> 迭代器
i1 = iter(r1)

# 输出: <range_iterator object at 0x0000023C9A7C54B0>
print(i1)

# 返回True
print("__iter__" in dir(i1))

# 返回True, 说明i1是一个迭代器
print("__next__" in dir(i1))

# 迭代器可以调用next()方法
# 输出: 0
print(next(i1))


# 定义生成器函数
def generator():
    for i in range(20):
        yield '娃哈哈%s' % i


# 调用生成器函数, 得到一个生成器
g = generator()

# 输出: <generator object generator at 0x00000192E96015E8>
print(g)

# 返回True
print('__iter__' in dir(g))

# 返回True, 说明g其实也是一个迭代器
print('__next__' in dir(g))

# 从生成器中读取数据
for i in range(20):
    print(next(g))

