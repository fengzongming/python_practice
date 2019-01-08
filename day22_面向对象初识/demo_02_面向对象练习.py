# 练习一：在终端输出如下信息
#
# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健
# 老张…

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def climb_mountain(self):
        print("%s, %s岁, %s, 上山去砍柴" % (self.name, self.age, self.sex))

    def driver_car(self):
        print("%s, %s岁, %s, 开车去东北" % (self.name, self.age, self.sex))

    def baojian(self):
        print("%s, %s岁, %s, 最爱大保健" % (self.name, self.age, self.sex))


p1 = Person("小明", 10, "男")
p2 = Person("老李", 90, "男")
p1.climb_mountain()
p1.driver_car()
p1.baojian()
p2.climb_mountain()
p2.driver_car()
p2.baojian()

