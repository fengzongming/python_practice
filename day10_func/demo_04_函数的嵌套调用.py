"""
    函数的嵌套调用

"""


def max2(a, b):
    return a if a > b else b


# 函数的嵌套调用
def three_max(x, y, z):
    c = max2(y, z)
    return max2(x, c)


# print(three_max(22, 11, 12))

a = 1

# print(a)

def wrapper():

    a = 6

    def outer():
        # a = 2

        def inner():
            # 想要修改全局变量的话, 使用global修饰即可
            # global a
            # a = 3

            # 如果想要修改上一层局部变量的值的话, 用nonlocal修饰
            # 只对最近的一层有影响
            nonlocal a
            a = 11
            print(a)

        inner()
        print(a)
    print(a)


wrapper()
