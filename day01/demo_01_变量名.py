"""
    变量(标识符)命名规则:
        1. 由字母, 数字, 下划线组成
        2. 严格区分大小写(基本所有语言都区分)
            如a和A不是同一个变量
        3. 数字不能开头
        4. 不能是python的关键字(一共有35个关键字)
        5. 不能是中文
            实际上, 在python3中, 是可以使用中文变量名的, 但是千万不要使用
        6. 可以是python中的内置函数, 但是命名为变量后, 无法再调用该函数
            如 print = 12, 就无法调用print()函数

        python中的关键字: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
        'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
        'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    常量命名规则:
        1. 一个单词时: 单词字母全部大写
            如: AGE = 20
        2. 多个单词时: 每个单词字母全部大写,使用下划线连接
            如: VALUE_OF_PAI = 3.1415926
        3. python中的常量可以修改, 不会报错,
           有些语言的话, 修改常量值会报错, 如java语音
"""

import keyword

# 打印python的关键字
# print(keyword.kwlist)
# print(len(keyword.kwlist))  # 35
# print(type(keyword.kwlist))  # <class 'list'>

# 正确的变量名
num1 = 1
_num2 = 2
number_of_students = 50

# 变量名严格区分大小写
a = 1
A = 2
print(a)
print(A)

# 错误的变量名
# 数字开头的变量
# 报错: SyntaxError: invalid syntax
# 12num = 3

# 错误的变量名
# python的关键字作为变量名
# 报错: SyntaxError: invalid syntax
# lambda = 12

# 错误的变量名
# 中文
# 可以使用中文变量名, 但是不要使用
# 姓名 = 'fzm'
# print(姓名)

# 变量可以是python中的内置函数
# sum函数是可以作为变量名使用
# print(sum([1, 2, 3]))
# sum = 123
# print(sum)

# 常量使用
AGE = 12
VALUE_OF_PAI = 3.1415926

print(AGE)  # 12
print(VALUE_OF_PAI)  # 3.1415926

# 但是我们可以修改常量的值
AGE = 11
print(AGE)  # 11
