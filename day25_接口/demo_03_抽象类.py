"""
    python中没有interface关键字, 只有class关键字
    所以实际上, python中的接口和抽象类都只用abc模块进行约束就可以了

    唯一的区别:
            接口里面定义的方法不要实现, 抽象类里面的方法可以实现, 可以不实现


"""
from abc import abstractmethod, ABCMeta

