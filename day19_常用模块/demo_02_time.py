"""
    时间:
        格式化时间  —— 字符串： 给人看的
        时间戳时间 —— float时间 ： 计算机看的
        结构化时间 —— 元祖 ：计算用的

    时间转化:

"""
import time

# 时间戳时间
print(time.time())

# 格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 结构化时间
print(time.localtime())

# 时间戳 -> 结构化时间
# time.localtime(时间戳)
print(time.localtime(time.time()))

# 结构化时间 -> 时间戳
# time.mktime(结构化时间)
print(time.mktime(time.localtime()))

# 结构化时间 -> 格式化时间
# time.strftime()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化时间 -> 结构化时间
print(time.strptime("2019-01-07 11:56:30", "%Y-%m-%d %H:%M:%S"))

