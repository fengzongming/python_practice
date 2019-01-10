"""
    isinstance(obj,cls)检查是否obj是否是类 cls 的对象, 传入cls的父类的话, 也会返回True
    issubclass(sub, super)检查sub类是否是 super 类的派生类

"""


class A(object):
    pass


class B(A):
    pass


class C(object):
    pass


a = A()
b = B()
print(isinstance(a, A))
print(isinstance(b, A))
print(issubclass(B, A))
print(issubclass(C, A))
