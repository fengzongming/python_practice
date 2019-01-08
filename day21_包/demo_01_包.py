"""
    导入包的时候, 其实就是执行包里面的__init__.py文件

"""


# 第一种情况: 导入比较深的时候
# from glance.api import policy
# policy.get()


# 绝对导入
# 第二种情况: 只导入包名, 但在包名及其子包里的__init__文件, 再导入模块
# 但第二种情况的问题是, 一旦把总包放在了另一个包里的话, 就要重写__init__文件
# import glance
# glance.api.policy.get()
# glance.cmd.manage.main()
# glance.db.models.register_models("mysql")


# 用glance2来理解相对导入
import glance2


# glance2.api.policy.get()
# glance2.cmd.manage.main()
# glance2.db.models.register_models("oracle")

