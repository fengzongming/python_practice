"""
         pickle
            支持的数据类型:
                所有的python中的数据类型都可以转化成字符串形式
            缺点:
                pickle序列化的内容只有python能理解
                且部分反序列化依赖python代码

"""
import pickle
import time

dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
str_dic = pickle.dumps(dic)
# 一串二进制内容
# 输出: b'\x80\x03}q\x00(X\x02\x00\x00\x00k1q\x01X\x02\x00\x00\x00v1q\x02X\x02\x00\x00\x00k2q\x03X\x02\x00\x00\x00v2q\x04X\x02\x00\x00\x00k3q\x05X\x02\x00\x00\x00v3q\x06u.'
# print(str_dic)

dic2 = pickle.loads(str_dic)
# 输出: <class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# print(type(dic2), dic2)

# struct_time = time.localtime()
# f1 = open("pickle_file2", "wb")
# pickle.dump(struct_time, f1)

# f2 = open("pickle_file2", "rb")
# struct_time2 = pickle.load(f2)
# print(struct_time2)
