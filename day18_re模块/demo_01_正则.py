"""
    正则模块学习

    正则作用: 匹配字符串内容的一种规则

    正则内容:
        1. 字符组  []
        2. 元字符 . \w \s \d \b ^ $ | () [^..]
        3. 量词 *+?{}

"""

import re

# 练习1: 在没学习正则之前, 判断用户输入的手机号是否合法
# phone_number = input("请输入你的手机号: ")
#
# if phone_number.isdigit() and \
#         len(phone_number) == 11 and \
#         phone_number.startswith("13") or \
#         phone_number.startswith("15") or \
#         phone_number.startswith("17") or \
#         phone_number.startswith("18"):
#         print("你的手机号合法, 你的手机号是: ", phone_number)
# else:
#     print("你输入的手机号非法")


# 0. 使用正则模块, 来判断手机号是否合法
# phone_number = input("请输入你的手机号: ")
# if re.match("^(13|15|17|18)\d{9}", phone_number):
#     print("你的手机号合法, 你的手机号是: ", phone_number)
# else:
#     print("你输入的手机号非法")


# 1. 字符组学习
# print(re.findall("[0-9]", "sakjhfajkfh8jasklfj"))
# print(re.findall("[a-z]", "sakjhfajkfh8jasklfj"))

# 2. 元字符
# . 匹配除换行符\n以外的任意字符
# print(re.findall(".", "\n"))    # []
# print(re.findall(".", "sss"))

# \w 匹配字母数字下划线
# print(re.findall("\w", "abc def_ghi()@#"))

# \s 匹配任意空白字符
# print(re.findall("\s", "  abc \t \n"))  # [' ', ' ', ' ', '\t', ' ', '\n']

# \d 匹配数字
# print(re.findall("\d", "qqww789zxc"))

# \b 匹配单词结尾
# print(re.findall(r"g\b", "egg zxcvg"))  # ['g', 'g']

# [^...] 匹配除了字符组中字符的所有字符
print(re.findall("[^a-z]", "AabcDE1678"))





