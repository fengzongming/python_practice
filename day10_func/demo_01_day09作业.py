# 1、写函数，检查获取传入列表的所有奇数位索引对应的元素，
# 并将其作为新列表返回给调用者。

def get_list(the_list):
    new_list = []

    for i in range(len(the_list)):
        if i % 2 == 1:
            ele = the_list[i]
            new_list.append(ele)

    return new_list


# 方法2
def get_list2(the_list):
    return the_list[1::2]


# res = get_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
# res2 = get_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(res)
# print(res2)


# 2、写函数，判断用户传入的值（字符串、列表、元组）长度是否大于5。
def get_length(the_list):
    return len(the_list) > 5


res = get_length([1, 2, 3, 4, 5, 6])
res2 = get_length([1, 2, 3, 4])
print(res)
print(res2)


# 3. 写函数，接收两个数字参数，返回比较大的那个数字。
# 使用三元运算符
def get_max(num1, num2):
    return num1 if num1 > num2 else num2


print(get_max(21, 32))
