# 1、写函数，接收n个数字，求这些参数数字的和。
def get_sum(*args):
    res = 0
    for i in args:
        res += i

    return res


print(get_sum(1, 2, 3, 4, 5))
