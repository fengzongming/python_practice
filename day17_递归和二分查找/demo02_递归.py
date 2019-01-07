"""
    递归:
        在函数中调用自身函数
        且每次调用时, 参数会不断变化, 向着结束的方向运行

    递归注意点:
        1. 写方法
        2. 确定出口条件
        3. 找规律

"""


# 用递归实现1~100的累加
def lei_jia(n):
    if n == 1:
        return 1
    return n + lei_jia(n - 1)


# print(lei_jia(100))

# 用递归实现阶乘
def jie_cheng(n):
    if n == 1:
        return 1
    else:
        return n * jie_cheng(n - 1)


# print(jie_cheng(5))

# 探究递归的深度
# 最多只能打印到996
def get_digui_length(n):
    print(n)
    get_digui_length(n + 1)


# get_digui_length(1)

# 修改递归的深度
import sys

# 打印python的递归限制: 1000
print(sys.getrecursionlimit())

# 修改python中的递归限制
sys.setrecursionlimit(2000)
get_digui_length(1)
