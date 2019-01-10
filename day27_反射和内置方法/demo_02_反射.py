"""
    hasattr: 检测属性和方法
    getattr: 获取属性和方法
    delattr: 删除属性和方法
"""
class Foo:
    f = '类的静态变量'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('hi,%s' % self.name)


obj = Foo('mike', 73)

# 检测对象是否有某属性和方法
print(hasattr(obj, "name"))
print(hasattr(obj, "say_hi"))

name = getattr(obj, "name", "没找到这个属性哦")
# 输出:mike
print(name)

sex = getattr(obj, "sex", "没找到年龄属性")
# 输出: 没找到年龄属性
print(sex)


# delattr(obj, "name")
# print(obj.name)

obj.say_hi()
delattr(obj, "say_hi")
# obj.say_hi()
