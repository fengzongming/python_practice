"""
    导入模块的流程:

        1. 先从sys.moudles的keys中查找
        2. 如果找到了，就不重复导入; 如果没有找到，就从sys.path中导入
        3. 导入后，创建这个模块的命名空间
        4. 执行文件，把文件中的名字都放到命名空间里

    导入模块的顺序:
        1. 先导入内置模块
        2. 导入第三方模块
        3. 导入自己写的模块

    导入模块的使用:
        1. import 模块
        2. import 模块 as 别名
        3. import 模块1, 模块2
        4. from 模块 import 变量名
            如导入的文件里, 有相同的变量名, 则被导入的模块的变量无法访问
        5. from 模块 import 变量名 as 别名
        6. from 模块 import 变量名1, 变量名2
        7. from 模块 import *
            与模块内的__all__相关, __all__是一个列表, 默认存储模块的所有变量名

"""

# import sys
# import time
# import demo
# demo.read()
# print(demo.money)


# import demo as d
# d.read()


# from demo import read
# read()
# def read():
#     print("demo 04 read")
# read()


from demo import *
read()
print(money)
