"""
    如果默认参数是一个可变数据类型(list, dict, set),
    那么每次调用这个函数,并且不给这个默认参数传值的话,
    每次都会公用这个数据类型的资源

"""


def func1(k, the_list=[]):
    the_list.append(1)
    print(the_list)


func1(1)  # [1]
func1(2)  # [1, 1]
func1(3)  # [1, 1, 1]
func1(4, [1, 2])  # [1, 2, 1]
