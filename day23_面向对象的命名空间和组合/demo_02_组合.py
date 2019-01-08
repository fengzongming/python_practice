"""
    组合: 一个类的对象的属性, 是另一个类的对象

"""

# 如person对象有生日属性, 生日属性也可以是一个类的对象


class Person(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday =birthday

class Birthday(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

b1 = Birthday(1994, 3, 1)
p1 = Person("小明", b1)
print(p1.name)
print(p1.birthday.year)
print(p1.birthday.month)
print(p1.birthday.day)