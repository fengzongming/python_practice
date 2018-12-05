"""
    bool数据类型
        bool -> int,  True: 1, False: 0
        int  -> bool,  非0: True, 0: False

        bool -> str,  True: "True", False: "False"
        str  -> bool, 非空字符串: True, 空字符串: False

"""

print(int(True))
print(int(False))

print(bool(-1))
print(bool(0))

print(str(True))
print(str(False))

print(bool("qwe"))
print(bool(""))