"""
    用户交互:
        1. 使用input()函数
        2. 可以在括号中输入, 提示用户输入的字符串
        3. 用户输入的数据, 都是字符串格式, 哪怕用户输入的数字, 其实也是字符串
        4. 可以使用type()函数查看变量的类型
        5. 可以使用数据类型, 强制转换用户输入的数组, 如把用户输入的数字, 转换为int类型
"""

# name = input("请输入你的姓名: ")
# print(name)

# 展示用户输入的都是字符串
# number = input("请输入你喜欢的数字: ")
# print(number)
# print(type(number))   # <class 'str'>

# 转换用户输入的数据类型, 方法1
# age = input("请输入你的年龄: ")
# print(age)
# print(type(age))    # <class 'str'>
#
# print("转换后")
# age = int(age)
# print(age)
# print(type(age))    # <class 'int'>


# 转换用户输入的数据类型, 方法2
# 直接转换
age = int(input("请输入你的年龄: "))
print(age)
print(type(age))    # <class 'int'>


