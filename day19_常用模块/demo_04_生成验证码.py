"""
    需求: 生成一个6位验证码, 包含英文和数字

"""

import random
import time

# 生成任意一个数字
code = ""
for i in range(6):
        num = random.randint(0, 9)
        letter = chr(random.randint(65, 90))
        temp = random.choice([num, letter])
        code = "".join([code, str(temp)])

print(code)