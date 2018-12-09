"""
    闭包的概念:
        内部函数使用外部函数的变量
        并且外部函数返回内部函数的变量名

"""


def outer():
    a = 1

    def inner():
        print(a)

    return inner


func = outer()
func()
