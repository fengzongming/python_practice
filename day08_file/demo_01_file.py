"""
    文件操作

"""

# "r" 以读模式读取文件
# f = open("练习文件", "r", encoding="utf-8")
# content = f.read()
# print(content)

# "rb"以二进制读模式读取文件
# f = open("练习文件", "rb")
# content = f.read()
# content = content.decode("utf-8")
# print(content)

f = open("练习文件2", "r+", encoding="utf-8")
print(f.read())
f.write("天使, 恶魔")
f.flush()
print(f.read())