"""
    re模块的方法

"""
import re

# findall(pattern, string, flags=0): # 返回所有满足匹配条件的结果,放在列表里
# list1 = re.findall("a", "abc aqwe aasd")
# print(list1)


# search(pattern, string, flags=0):
# 函数会在字符串内查找模式匹配,直到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
# group1 = re.search("[\d]", "qwerkjh8")
# print(group1)   # <re.Match object; span=(7, 8), match='8'>
# if group1:
#     print(group1.group())


# match(pattern, string, flags=0):
# 同search,不过仅在字符串开始处进行匹配
# group2 = re.match("\w", " thanks")
# if group2:
#     print(group2.group())
# else:
#     print("未匹配到")


# split(pattern, string, maxsplit=0, flags=0):
# 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
# res = re.split("[ab]", "abcd")
# print(res)

# sub(pattern, repl, string, count=0, flags=0):
# 用pattern在string中正则匹配, 用repl替换找到的字符串, count代表替换次数
# demo: #将数字替换成'W'，参数1表示只替换1个
# res = re.sub("\d", "W", "qqwweerr55tt66", 1)
# print(res)


# subn(pattern, repl, string, count=0, flags=0):
# 返回的是一个元组,(替换后的字符串, 替换的次数)
# 返回的是匹配到的次数
# res = re.subn("\d", "W", "qqwweerr55tt66", 1)
# print(res)


# compile(pattern, flags=0):
# pattern = re.compile("\d{3}")
# print(type(pattern))    # <class 're.Pattern'>
# res = pattern.search("qwe123zcx")
# if res:
#     print(res.group())


# finditer(pattern, string, flags=0):
# 返回的是一个存放匹配结果的迭代器
res = re.finditer("\d", "qwe123zxc567xx")
print(type(res))    # <class 'callable_iterator'>
print(next(res).group())    # 查看第一个结果
print(next(res).group())    # 查看第二个结果
print([i.group() for i in res])     # 查看剩余的结果






