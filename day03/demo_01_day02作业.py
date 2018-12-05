# 计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和
num = 0
res = 0
while num <= 98:
    num += 1
    if num == 88:
        continue
    if num % 2 == 1:
        res += num
    else:
        res -= num
print(res)
