"""
    封装:
        声明变量或者方法时, 加上"__", 就可以将属性/方法改为私有属性

        外界调用:
            可以通过对象._类__私有属性名访问到私有属性, 但不推荐使用
            可以通过对象._类__私有方法名()访问到私有方法, 但不推荐使用
"""


class Person(object):
    __key = 123

    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def get_pwd(self):
        return self.__password

    def __tell(self):
        print("这是私有方法")


p1 = Person("mike", "666")

# 输出: {'name': 'mike', '_Person__password': '666'}
print(p1.__dict__)

# 可以通过对象._类__私有属性名访问到, 但不推荐使用
print(p1._Person__password)

print(p1.get_pwd())

# 调用对象的私有方法
p1._Person__tell()

print(p1._Person__key)
