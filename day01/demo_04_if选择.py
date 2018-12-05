"""
    if选择结构:
        格式1: 只判断一种情形
            if 条件:
                条件为True时, 才会执行内部代码

        格式2: 只有两种情形
            if 条件:
                内部代码1
            else:
                内部代码2

        格式3: 有多种情形(大于两种)
            if 条件1:
                内部代码1
            elif 条件2:
                内部代码2
            ...
            elif 条件n:
                内部代码n
            else:
                内部代码n + 1





"""

# 练习if格式1
# age = 18
# if age >= 18:
#     print("已成年, 你可以去网吧了")


# 练习if格式2
# 题目: 判断用户输入的是奇数还是偶数
# number = int(input("请输入一个你喜欢的数字: "))
# if number % 2 == 0:
#     print("我猜你输入的是偶数")
# else:
#     print("我猜你输入的是奇数")

# 练习if格式3
# 题目: 根据用户输入的分数, 判断用户的分数等级
# 其中 85 <= 分数 <= 100, 为优秀
#      70 <= 分数 < 85,   为良好
#      60 <= 分数 < 70,   为及格
#       0 <= 分数 < 60,   为不及格
score = int(input("请输入你的分数: "))
if score >= 85:
    print("你的成绩是优秀")
elif score >= 70:
    print("你的成绩是良好")
elif score >= 60:
    print("你的成绩是及格")
else:
    print("你的成绩是不及格, 要加油哦")

