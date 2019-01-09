"""
    继承:
        继承表达的是一种 子类是父类的关系
    继承作用:
        减少代码量

    __bases__: 只有类才具有的属性(对象没有), 用于记录父类, 只记录一层

    派生
        派生属性:
            父类中没有的属性, 在子类中出现, 叫做派生属性
        派生方法:
            父类中没有的方法, 在子类中出现, 叫做派生方法

    子类对象调用:
        只要是子类的对象调用，子类中有的名字, 一定用子类的，
        子类中没有才找父类的，如果父类也没有报错

    子类调用父类:
        方法1. 父类名.方法名 需要自己传self参数
        方法2. super().方法名 不需要自己传self


"""


class A(object):
    pass


class B(object):
    pass


class A_son(A):
    pass


class A_B_son(A, B):
    pass


print(A.__bases__)
print(A_son.__bases__)
print(A_B_son.__bases__)


class Animal(object):
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def eat(self):
        print("%s正在吃饭" % self.name)

    def drink(self):
        print("%s正在喝水" % self.name)


class Dog(Animal):

    def eat(self):
        super().eat()
        print("%s正在啃骨头" % self.name)

    def bark(self):
        print("%s正在狂吠" % self.name)


class Cat(Animal):
    def climb(self):
        print("%s 正在爬树" % self.name)


dog1 = Dog("二哈", "旺财")
cat1 = Cat("波斯猫", "旺运")
dog1.eat()
dog1.drink()
dog1.bark()
cat1.eat()
cat1.drink()
cat1.climb()
