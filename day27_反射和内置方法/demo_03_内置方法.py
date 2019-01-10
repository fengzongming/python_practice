"""
    __str__(): 对象
"""
class Teacher:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # def __str__(self):
    #     return "Teacher's object :%s" % self.name

    def __repr__(self):
        return str(self.__dict__)

    def func(self):
        return 'wahaha'


t = Teacher("qq", 1000)
print(t)
print(repr(t))
