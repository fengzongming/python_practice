"""
1、元素分类
    有如下值li= [11,22,33,44,55,66,77,88,99,90]，
    将所有大于 66 的值保存至字典的第一个key中，
    将小于 66 的值保存至第二个key的值中。

    即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
"""

# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# li2 = []
# li3 = []
# dic = {"k1": li2, "k2": li3}
# for i in li:
#     if i > 66:
#         li2.append(i)
#     elif i < 66:
#         li3.append(i)
#
# print(dic)


"""
2、输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = ["手机", "电脑", '鼠标垫', '游艇']
要求：1：页面显示 序号 + 商品名称，如：
      	1 手机
	   	2 电脑
     	…
     2： 用户输入选择的商品序号，然后打印商品名称
     3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
     4：用户输入Q或者q，退出程序。
"""
li = ["手机", "电脑", '鼠标垫', '游艇']

flag = True

while flag:

    # 输出商品列表
    for i in li:
        print(li.index(i) + 1, i)

    user_choice = input("请输入你要购买的产品的的序号, 输入Q/q, 则退出程序: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if abs(user_choice) < len(li):
            print(li[user_choice - 1])
            break
        else:
            print("您输入的序号有误, 请重新选择!")
            continue
    else:
        if user_choice.lower() == 'q':
            print("系统已退出")
            break
        else:
            print("您输入的序号有误, 请重新选择!")
            continue