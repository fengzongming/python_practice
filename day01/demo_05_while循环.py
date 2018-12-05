"""
    while循环
        continue
        break
"""

# 计算1+2+3+...+100
res = 0
num = 1
while num <= 100:
    res += num
    num += 1
print(res)


# 使用内置函数, 计算1+2+3+..+100
print(sum(range(101)))
