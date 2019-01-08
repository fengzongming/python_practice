class Person(object):
    def __init__(self, *args):
        print("run init")
        self.name = args[0]
        self.hp = args[1]
        self.aggr = args[2]
        self.sex = args[3]

    def walk(self, n):
        print("%s走了%s步" % (self.name, n))

p1 = Person("娃娃", 100, 10, "女")
print(p1.__dict__)
print(p1.name)
p1.__dict__['name'] = "二哈"
print(p1.__dict__)
print(p1.name)

# self必须带着的原因
p1.walk(2)
Person.walk(p1, 3)