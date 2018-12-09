"""
修改user_info中的密码
把123456修改为admin
"""

import os

with open("user_info", "r", encoding="utf-8") as f1, open("user_info.bak", "w", encoding="utf-8") as f2:
    for line in f1:
        if "123456" in line:
            line = line.replace("123456", "admin")
        f2.write(line)

os.remove("user_info")
os.rename("user_info.bak", "user_info")
