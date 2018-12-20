"""
    # 某个方法属于某个数据类型的变量，就用.调用
    # 如果某个方法不依赖于任何数据类型，就直接调用  内置函数 和 自定义函数
"""
# 返回本地作用域中的所有名字
# print(locals())

# 返回全局作用域中的所有名字
# print(globals())


# next(): 得到生成器中的元素
# 迭代器.__next__()

# 使用生成器表达式得到生成器g
g = (i for i in range(10))

# 使用.__next__()方法得到生成器里的元素, 输出: 0
# print(g.__next__())

# 使用.__next__()方法得到生成器里的元素, 输出: 1
# print(next(g))


# iter(): 把可迭代对象转换成迭代器
# 可迭代对象.__iter__()
# r1 = range(10)
# ri1 = iter(r1)
# ri2 = r1.__iter__()
# print(ri1)
# print(ri2)


# dir(): 查看一个变量拥有的方法
# print(dir([]))
# print(dir(123))


# help(): 查看方法的使用说明
# print(help(str))


# import 模块 : 导入模块
# __import__('模块名')

# import time
# time.time()

# t = __import__('time')
# print(t.time())


# id(): 获取对象的内存地址, 返回值是int类型
# print(id([]))
# print(type(id([])))


# hash(): 获取不可变对象的hash值, 在每次执行过程中, 对象的hash值不会变
# print(hash("hello"))
# print(hash("asd"))
# print(hash("asd"))

# 如果对可变对象进行哈希, 则会报错
# TypeError: unhashable type: 'list'
# print(hash([]))


# input(): 用户交互输入


# print(): 打印
# 参数:
#       end:指定输出的结束符, 默认是换行符
#       sep: 输出多个值之间的分隔符
# print("hello", end="\t")
# print(1, 2, 3, 4, 5, sep="|")


# exec()
# eval()
# 都可以执行字符串类型的代码
# 区别: eval有返回值, exec没有返回值

# 输出: hello
# exec("print('hello')")
# 输出: world
# eval("print('world')")

# 输出: None
# print(exec("1 + 2 + 3 + 4"))
# 输出: 10
# print(eval("1 + 2 + 3 + 4"))


# 和计算相关的函数
print(bin(10))
print(oct(10))
print(hex(10))

# 返回商和余数组成的元组
print(divmod(7, 2))

print(pow(2, 3))
print(sum([1, 2, 3, 4, 5]))
print(min(11, 2, 3, 5, 1))
print(min([11, 2, 1, 1, 4, 5, 6, 0]))

# 输出: -1, 因为参数key为abs, 所以比较的是绝对值的最小值
print(min([11, 2, 21, 31, 4, 5, -1, -11], key=abs))

