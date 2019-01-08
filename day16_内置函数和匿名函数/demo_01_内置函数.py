# reversed(): 不改变原来的可迭代对象，返回一个新的反向的迭代器

list1 = [1, 2, 3, 4, 5]


# 输出: [1, 2, 3, 4, 5]
# print(list1)

# 调用list的reverse()方法, 使列表逆序
# list1.reverse()
# 输出: [5, 4, 3, 2, 1]
# print(list1)

# 通过reversed()函数, 得到的列表是一个迭代器
# list2 = reversed(list1)

# 输出: <list_reverseiterator object at 0x0000000001DC80B8>
# print(list2)
# print(list1)

# 输出: True, 说明list2是一个迭代器
# print("__iter__" in dir(list2) and "__next__" in dir(list2))

# 输出: 1
# print(list2.__next__())
# 输出: 2
# print(next(list2))


# format函数
# print(format('test', '<20'))
# print(format('test', '>40'))
# print(format('test', '^40'))


# bytes(): 将字符串转换成bytes类型

# unicode转换成GBK的bytes
# print(bytes("你好", encoding="GBK"))

# unicode转换成utf-8的bytes
# print(bytes("你好", encoding="UTF-8"))


# # bytearray(): 将字符串转换成bytes类型, 并可以根据索引取出每个字符
# b_array = bytearray('你好', encoding='UTF-8')
# print(b_array)
# print(b_array[0])


# ord(): 返回指定字符的索引
# chr(): 返回指定索引的字符
# ascii(): 返回字符串的索引
# print(ord('好'))
# print(ord('1'))
# print(chr(97))
# print(ascii('你好'))
# print(ascii('1'))


# repr(): 按照原样输出, 字符串会带上引号
# name = 'egg'
# print('你好%r' % name)
# dic2 = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# print(name)
# print(repr(name))


# all(): 判断可迭代对象中, 是否含有False的元素, 有就返回False, 没有才返回True
# 特殊情况: 当传入空列表和空元组的时候, 也会返回True
# 返回: False
# print(all([1, 2, 3, ""]))

# 返回: False
# print(all([0, 2, 3, "test"]))

# 返回: False
# print(all(range(10)))

# 返回: True
# print(all(range(1, 10)))

# 返回: True
# print(all([]))

# 返回: True
# print(all(()))

# any(): 判断可迭代对象中, 是否含有True的元素, 若有则返回True
# 返回: True
# print(any([1, 2, 0]))

# 返回: False
# print(any([]))

# 返回: False
# print(any(()))


# zip(): 将可迭代对象, 按照相同索引的位置, 拼接起来, 组成一个个新的元组
# 按照最短长度的元组拼接
# l = [1, 2, 3, 4, 5]
# l2 = ['a', 'b', 'c', 'd']
# l3 = ('*', '**', [1, 2])
# d = {'k1': 1, 'k2': 2, 'k3': 3}
# for i in zip(l, l2, l3, d):
#     print(i)


# filter(): 对可迭代对象中的每个元素, 使用函数处理

def is_odd(num):
    return num % 2 != 0


ret = filter(is_odd, [1, 2, 3, 4, 5, 6])

# 返回True, 说明filiter()得到的对象是一个迭代器
# print("__next__" in dir(ret))
# print("__iter__" in dir(ret))
#
# print(ret)
#
# for i in ret:
#     print(i)

# map():
ret2 = map(is_odd, [1, -2, 3, 4, -5, 6])

# 返回True, 说明map()得到的对象是一个迭代器
print("__next__" in dir(ret2))
print("__iter__" in dir(ret2))

for i in ret2:
    print(i)



