"""
    可迭代的:
        只要含有__iter__的方法都是可迭代的

    迭代器:
        1. 可迭代的对象通过__iter__()方法, 调用的返回值就是一个迭代器
        2. 迭代器通过__next__()方法, 从迭代器中一个一个的转换

    迭代器的好处：
        1. 从容器类型中一个一个的取值，会把所有的值都取到。
        2. 节省内存空间
        3. 迭代器并不会在内存中再占用一大块内存，
            随着循环, 每次生成一个
            每次next每次给我一个
"""

# 返回True
print("__iter__" in dir([]))

# 返回False
print("__next__" in dir([]))

# 返回True
print("__iter__" in dir([].__iter__()))

# 返回True
print("__next__" in dir([].__iter__()))

# <class 'list_iterator'>
print(type([].__iter__()))

# 返回False
# 说明range()函数只是一个可迭代的对象, 不是迭代器
print("__next__" in dir(range(10)))
