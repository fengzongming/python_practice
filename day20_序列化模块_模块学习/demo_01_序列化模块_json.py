"""
    序列化概念: 将原本的字典、列表等内容转换成一个字符串的过程

    序列化:
        数据类型 -> 字符串
    反序列化:
        字符串 -> 数据类型

    python中有三个模块, 用于处理序列化相关的问题
        json
            支持的数据类型:
                (数字, 字符串, 列表, 字典, 元组)
            优点:
                它是通用的序列化格式
            缺点:
                只有很少一部分数据类型能够通过json转化成字符串

        pickle
            支持的数据类型:
                所有的python中的数据类型都可以转化成字符串形式
            缺点:
                pickle序列化的内容只有python能理解
                且部分反序列化依赖python代码
        shelve
            优点:
                序列化句柄
                可以使用句柄直接操作，非常方便

"""
import json

dic1 = dict([("k1", "v1"), ("k2", "v2"), ("k3", "v3")])

# 序列化: 将一个字典转换成一个字符串
# str_dic1 = json.dumps(dic1)
# 输出结果: <class 'str'> {"k1": "v1", "k2": "v2", "k3": "v3"}
# print(type(str_dic1), str_dic1)

# 反序列化: 将一个字符串格式的字典转换成一个字典
# dic2 = json.loads(str_dic1)
# 输出: <class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# print(type(dic2), dic2)

# list_dic = [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]

# 序列化: 将嵌套的数据类型序列化
# str_dic = json.dumps(list_dic)
# 输出: <class 'str'> [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]
# print(type(str_dic), str_dic)
# list_dic2 = json.loads(str_dic)
# print(type(list_dic2), list_dic2)


# dump和load方法
# dump: 直接将序列化的结果写入到文件里
# f = open("json_file1", "w", encoding="utf-8")
# dic1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# json.dump(dic1, f)

# load: 将文件里的内容反序列化出来
# f = open("json_file1", "r", encoding="utf-8")
# dic2 = json.load(f)
# print(type(dic2), dic2)
