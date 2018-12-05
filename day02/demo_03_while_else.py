"""
    while else的使用
        如果while循环, 是正常结束的话, 会执行else里面的代码块
        如果while循环, 是被break结束掉, 就不会执行else里面的代码块

"""

num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("开始新的区域")
print("不是else的部分")


# else不执行
# num = 1
# while num <= 5:
#     print(num)
#     if num == 3:
#         break
#     num += 1
# else:
#     print("开始新的区域")
# print("不是else的部分")

