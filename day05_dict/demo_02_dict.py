"""
    dict
        数据类型划分: 可变数据类型, 不可变数据类型
            不可变(可哈希): 元组, bool, int, str
            可变(不可哈希): list, dict, set

    dict的key:   必须是不可变数据类型(可哈希)
    dict的value: 任意数据类型

    dict的优点: 二分查找去查询
    dict的特点: 无序
"""

# 练习dict的key, value允许的数据类型
# dic = {"name": "fzm", "age": 24, 666: "good", (1, 2, 3): [4, 5, 6], True: {False: {2}}}
# print(dic)

dic = {"name": "fzm", "age": 24, 666: "good"}

# 增加操作/修改操作
# 如果是dic中没有的key,则是新增
# dic["job"] = "CEO"
# print(dic)

# 如果是dic中已存在的keym 则是修改
# dic["name"] = "cindy"
# print(dic)

# setdefault(key, value): 有键值对，不做任何改变，没有才添加。
# dic.setdefault("age", 18)
# print(dic)

# 删除操作: pop, popitem, clear, del

# pop(key)
# dic.pop(666)
# print(dic)

# popitem(): 随机返回并删除字典中的一对键和值
# res = dic.popitem()
# print(res)
# print(dic)


# 修改操作
# update(): 把字典dic的键/值对更新到dic2里
# dic = {"name": "jin", "age": 18, "sex": "male"}
# dic2 = {"name": "alex", "weight": 75, "sex": "female"}
# dic2.update(dic)
# print(dic)
# print(dic2)


# 查询操作: keys(), values(), items(). get()
for i in dic:
    print(i)

print("*" * 50)

for i in dic.keys():
    print(i)

for i in dic.values():
    print(i)

print("*" * 50)

for key, value in dic.items():
    print(key)
    print(value)

print(dic.get("name"))
print(dic.get("name2", "没有这个键"))