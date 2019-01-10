"""
    @proerty装饰器是加在类的方法上,
    对象在调用时, 就可以使用"对象.方法名"去调用方法

    @方法名.setter: 修改
    @方法名.deleter: 删除

"""
from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.radius


c1 = Circle(1)
print(c1.area)
print(c1.perimeter)


# 没有加@方法名.setter不能赋值
# c1.area = 123

class Animal(object):
    def __init__(self, kind):
        self.kind = kind


class Person(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name

p1 = Person("mike")
print(p1.name)
p1.name = "cindy"
print(p1.name)

#
del p1.name

# 调用完删除方法后, 就无法获取name了
print(p1.name)

