"""
    str数据类型
        索引: 默认从0开始
        切片: [开始字符:结束字符:步长]
        字符串函数
"""

str1 = "aBcDEfg"

# 索引
# 根据索引取值
# print(str1[0])

# 切片
# 左闭右开
# print(str1[:])
# print(str1[0:3])
# print(str1[:-1])
# print(str1[::2])
# print(str1[::-1])

# 字符串的函数


# capitalize(): 首字母大写
# 注意: 如果第一个字符是非英文字母(中文/数字/特殊字符)的话, 字符串就不会变化
# 返回值: 有返回值
# 改变原对象: 不改变
# s = "#大1fZm123MiKe3"
# s1 = s.capitalize()
# print(s)
# print(s1)


# upper(): 单词全部大写
# lower(): 单词全部小写
# 返回值: 有返回值
# 改变原对象: 不改变
# s = "#大1fZm123MiKe3"
# s1 = s.upper()
# s2 = s.lower()
# print(s)
# print(s1)
# print(s2)


# swapcase(): 大小写翻转
# 返回值: 有返回值
# 改变原对象: 不改变
# s = "#大1fZm123MiKe3"
# s1 = s.swapcase()
# print(s)
# print(s1)


# title(): 每个隔开(特殊字符或者数字)的单词首字母大写
# 返回值: 有返回值
# 改变原对象: 不改变
# s = 'fade,crazy*w4rri0r_songsong node_3'
# s1 = s.title()
# print(s)
# print(s1)


# center(length, '空白字符')
# 只能传入单个字符(汉字/数字/英文字母/特殊字符)
# 返回值: 有返回值
# 改变原对象: 不改变
# s = "#大1fZm123MiKe3"
# s1 = s.center(20, '')
# print(s)
# print(s1)


# 公共方法:
# len(): 求长度
# s = "#大1fZm123MiKe3"
# print(len(s))


# startswith(): 判断字符串以什么开始
# endswith: 判断字符串以什么结束
# s = "#大1fZm123MiKe3"
# print(s.startswith("#大"))
# print(s.endswith("e3"))


# find():  通过元素找索引, 找不到就返回-1
# index(): 通过元素找索引, 找不到就报错
# s = "#大1fZm124MiKe3"
# print(s.find("3"))
# print(s.find("x"))
#
# print(s.index("3"))
# print(s.index("x"))


# strip rstrip lstrip: 去空格, 用户输入的时候, 可以去掉用户的空格
# print(" 123 ".strip())


# count(): 统计某个字符串在另一个字符串中, 出现的次数
# s = 'mikeMi fzmi'
# s1 = s.count('mi')
# print(s1)


# split(): 根据某个字符进行分割, 并把分割的字符删掉
# str ----> list
# s = 'a;alex;wusir;taibai'
# list2 = s.split("a")
# print(list2)


# format(): 格式化输出的3种方式
# s = '我叫{}，今年{}，再说一下我叫{}'.format('fzm', 24, 'fzm')
# print(s)
#
# s1 = '我叫{0}，今年{1}，再说一下我叫{0}'.format('fzm', 24)
# print(s1)
#
# s2 = '我叫{name}，今年{age}，再说一下我叫{name}'.format(name='fzm', age=24)
# print(s2)


# replace(old_str, new_str, times): 使用新的字符串替换旧的字符串
s = "aabbccaaddeeaaxxzz"
s11 = s.replace('aa', 'QQ', 1)
print(s)
print(s11)
