# 函数
# 顺序：位置参数，*args, 默认参数, **kwargs


# 位置函数
# 直接定义参数
def func1(name):
    print("hello", name)


# func1("mike")


# 默认参数
def func2(name="admin", age=22):
    print(name, age)


# func2()
# func2(name="fzm", age=24)
# func2(age=18, name="lx")


# 位置参数, 默认参数
def func3(name, age=20):
    print(name, age)


# func3("qq", 18)


# 动态参数
def func4(*args):
    for i in args:
        print(i)


# 可直接传多个参数
# func4(1, 2, 34)

# 传入元组的话, 需要加*
# tu1 = (6, 7, 8, 9)
# func4(*tu1)


def func5(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


func5(name="cc")


# dic1 = {"name": "qqc", "age": 12}
# func5(**dic1)


# 最完整的函数定义:
#   顺序参数, 动态参数(*args), 默认参数, 动态参数(**kwargs)
def func6(name, *args, sex="male", **kwargs):
    print(name)

    for i in args:
        print(i)

    print(sex)

    for k, v in kwargs.items():
        print(k, v)


func6("java", "ruby", "go", sex="female", job="CEO", salary=1000000)
