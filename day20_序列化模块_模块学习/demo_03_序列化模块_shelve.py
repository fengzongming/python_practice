"""
        shelve
            优点:
                序列化句柄
                可以使用句柄直接操作，非常方便

"""
import shelve

f1 = shelve.open('shelve_file3')
# 直接对文件句柄操作，就可以存入数据
# f1['key'] = {'int': 10, 'float': 9.5, 'string': 'Sample data'}
# f1.close()

# 直接用key值, 就可以取出数据了
f2 = shelve.open("shelve_file3")
print(f2["key"])

