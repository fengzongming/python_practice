"""
encode编码:
    将str -> bytes

"""

s1 = "mike"
print(s1.encode("utf-8"))   # b'mike'
print(s1.encode("gbk"))     # b'mike'

s2 = "你好"
print(s2.encode("utf-8"))   # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(s2.encode("gbk"))     # b'\xc4\xe3\xba\xc3'