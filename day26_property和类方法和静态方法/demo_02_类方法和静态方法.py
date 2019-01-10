"""
    类方法:   处理类相关属性的, 传参, 第一个参数是cls
    静态方法: 对参数没有要求, 不用传self或者cls

"""


class Goods(object):
    __discount = 0.8

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * Goods.__discount

    @classmethod
    def change_discount(cls, discount):
        cls.__discount = discount

    @staticmethod
    def show():
        print("静态方法不用传参数")


apple = Goods("苹果", 5)
print("苹果的单价: ", apple.price)
print("打折后")

Goods.change_discount(0.6)
print("苹果的单价: ", apple.price)

apple.change_discount(0.5)
print("苹果的单价: ", apple.price)

Goods.show()
apple.show()
