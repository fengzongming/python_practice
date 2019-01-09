"""
    python中定义接口:
        1. 定义类时, 在括号里加上metaclass=ABCMeta
        2. 在方法上使用@abstractmethod装饰器修饰

    python中定义接口类的作用:
        让子类有统一的方法名, 开发规范

"""

from abc import abstractmethod, ABCMeta


class Payment(object, metaclass=ABCMeta):

    @abstractmethod
    def pay(self, money):
        pass


class Wechat(Payment):
    def pay(self, money):
        print('已经用微信支付了%s元' % money)


class Alipay(Payment):
    def pay(self, money):
        print('已经用支付宝支付了%s元' % money)


class Applepay(Payment):
    def pay(self, money):
        print('已经用applepay支付了%s元' % money)


a1 = Alipay()
w1 = Wechat()
ap1 = Alipay()
a1.pay(10)
w1.pay(20)
ap1.pay(30)
