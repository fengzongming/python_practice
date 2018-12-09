username = input("请输入你要注册的用户名: ").strip()
password = input("请输入你要注册的密码: ").strip()

# 将用户注册的用户名和密码写入到文件里
with open("user_info", "w", encoding="utf-8") as f:
    info = "{}\n{}".format(username, password)
    f.write(info)
print("恭喜你, 注册成功")

print("欢迎来到XXX系统")

user_list = []

with open("user_info", "r", encoding="utf-8") as f2:
    for i in f2:
        user_list.append(i)

chance = 3

while chance > 0:
    username2 = input("请输入用户名: ").strip()
    password2 = input("请输入密码: ").strip()
    if (user_list[0].strip() == username2) and (user_list[1].strip() == password2):
        print("恭喜登录成功")
        break
    else:
        if chance == 0:
            print("输入密码错误次数太多, 账号已被锁住")
            break
        else:
            chance -= 1
            print("用户名或密码错误, 你还有%d次机会" % chance)
