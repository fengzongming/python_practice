class F:
    def func(self):
        print('F')


class A(F):
    pass


class B(A):
    pass


class E(F):
    pass


class C(E):
    pass


class D(B, C):
    pass



print(D.mro())
