# 1、使用while循环输入 1 2 3 4 5 6 8 9 10
# num = 0
# while num <= 9:
#     num += 1
#     if num == 7:
#         continue
#     print(num, end=" ")


# 输出 1-100 内的所有奇数
# num = 1
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#     num += 1

# 求1-2+3-4+5 ... 99的所有数的和
# num = 1
# res = 0
# while num <= 99:
#     if num % 2 == 0:
#         res += num
#     else:
#         res -= num
#
#     num += 1
#
# print(res)

# 6、用户登陆（三次机会重试）
# 账号: admin, 密码: 123456

num = 3
while num >= 1:
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    if (username == "admin") and (password == "123456"):
        print("登录成功")
        break
    else:
        num -= 1
        if num == 0:
            print("输入密码错误次数过多, 账号被锁定")
        else:
            print("用户名或密码错误, 你还有%d次机会" % num)
