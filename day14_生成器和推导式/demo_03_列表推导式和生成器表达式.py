"""
    列表推导式
        格式: [每一个元素或者是和元素相关的操作 for 元素 in 可迭代数据类型]

    生成器表达式
        可以通过生成器表达式, 直接得到一个生成器

"""

# 需求: 输出: 鸡蛋n, n从0累加到9
# 方法1: 使用for循环当然可以
# 方法2: 列表推导式
egg_list = ['鸡蛋%s' % i for i in range(10)]
print(egg_list)

# 需求: 输入0~9的平方和, 组成的列表
list1 = [i * i for i in range(10)]
print(list1)


# 生成器表达式
g = (i for i in range(10))

# 输出: <generator object <genexpr> at 0x0000020CADBB65E8>
print(g)

# 输出: <class 'generator'>
print(type(g))

# 调用生成器的__next__()方法
ret1 = g.__next__()

# 输出: 0
print(ret1)
