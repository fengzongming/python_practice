"""
    python中的多继承

"""
from abc import abstractmethod, ABCMeta


class Swim_Animal(object, metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class Walk_Animal(object, metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class Fly_Animal(object, metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(Swim_Animal, Walk_Animal):
    def swim(self):
        pass

    def walk(self):
        pass


class Bird(Swim_Animal, Fly_Animal):
    def swim(self):
        pass

    def fly(self):
        pass


t1 = Tiger()
b1 = Bird()
