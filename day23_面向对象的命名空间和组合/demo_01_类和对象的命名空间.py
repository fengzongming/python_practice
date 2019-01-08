"""
    类里可以定义两种属性
        1. 静态属性
            直接在类中定义的变量
        2. 动态属性
            类中定义的方法

    当对象创建时, 未指定与类的静态属性相同名称的属性时,
    对象可以直接访问类的静态属性

    对象无法修改类的静态属性
"""

class Course(object):
    language = ['Chinese']

    def __init__(self, name):
        self.name = name

c1 = Course("python")
c2 = Course("java")
print(c1.name)
print(c2.name)
print(c1.language)
print(c2.language)
print(Course.language)

c1.language = "python language"
print(c1.language)
print(c2.language)
print(Course.language)


