"""

"""
import random

# 输出: 0 < x < 1
print(random.random())

# 输出: 1 < x < 3
print(random.uniform(1, 3))

# 输出: 1 <= x <= 2
print(random.randint(1, 2))

# 输出: 1 <= x < 5
print(random.randrange(1, 5))

# 随机返回一个
print(random.choice([1, '23', [4, 5]]))

# 随机返回多个
print(random.sample([1, '23', [4, 5]], 2))

list1 = [1, 3, 5, 7, 9]
print(list1)

# 打乱列表
random.shuffle(list1)
print(list1)

