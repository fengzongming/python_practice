"""
    推导式进阶:
        [每一个元素或者是和元素相关的操作 for 元素 in 可迭代类型]
        [满足条件的元素或者是和元素相关的操作 for 元素 in 可迭代类型 if 元素相关的条件]

        # 可以把嵌套的可迭代对象, 全部拆出来
        [满足条件的元素或者是和元素相关的操作 for 可迭代对象1 in 可迭代类型 for 元素 in 可迭代对象 if 元素相关的条件]
"""

# 带条件的列表推导式, 需求: 30以内所有能被3整除的数
list1 = [i for i in range(31) if i % 3 == 0]
print(list1)

# 带条件的列表推导式, 需求: 30以内所有能被3整除的数的平方
list2 = [i ** 2 for i in range(31) if i % 3 == 0]
print(list2)

# 嵌套列表推导式, 需求: 找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
list3 = [name for name_list in names for name in name_list if name.count('e') == 2]
print(list3)

# 字典推导式, 需求: 将一个字典的key和value对调
dic1 = {'a': 10, 'b': 34}
new_dic = {dic1[key]: key for key in dic1}
print(new_dic)

# 字典推导式, 需求: 合并大小写对应的value值，将k统一成小写
dic2 = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
new_dic2 = {key.lower(): dic2.get(key.lower(), 0) + dic2.get(key.upper(), 0) for key in dic2}
print(new_dic2)
