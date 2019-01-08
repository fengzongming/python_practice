"""
    namedtuple: 使用名字来访问元素内容的tuple
    queue: 队列
    deque: 双向队列
    OrderdDict: 有序字典, 按照插入顺序排序

"""
from collections import namedtuple
import queue
from collections import deque
from collections import  OrderedDict

# 用namedtuple表示一个坐标点
# Point = namedtuple("Point", ["x", "y"])
# p = Point(1, 2)
# print("横坐标:", p.x)
# print("纵坐标:", p.y)

# 用namedtuple表示一个圆
# Circle = namedtuple("Circle", ["x", "y", "radius"])
# c1 = Circle("1", "1", "5")
# print("横坐标:", c1.x)
# print("纵坐标:", c1.y)
# print("半径:", c1.radius)


# queue 队列
# q = queue.Queue()
# q.put([1, 2, 3])
# q.put(4)
# q.put(5)
# q.put(6)
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

# 如果get的次数大于put的次数, 则队列会阻塞, 一直运行, 不会退出
# print(q.get())


# deque: 双向队列
# dq = deque([1, 2, 3])
# dq.append(4)
# dq.appendleft(5)
# dq.insert(1, 11)
# print(dq)
# num1 = dq.pop()
# num2 = dq.popleft()
# print(num1)
# print(num2)


# OrderdDict: 有序字典
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# d1 = dict([('a', 1), ('b', 2), ('c', 3)])
# for i in od:
#     print(i, od.get(i))


# defaultdict


