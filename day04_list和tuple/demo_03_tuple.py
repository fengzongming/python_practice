# 元组: 只读列表, 可循环查询, 可切片

tu = (1, 2, 3, 'alex', [2, 3, 4, 'taibai'], 'egon')

# 循环查询
# for i in tu:
#     print(i)

# 元组不能修改元素,
# 如果元素是可变元素的话, 可以修改元组的子元素的子元素
# 报错: TypeError: 'tuple' object does not support item assignment
# tu[0] = 111

# 修改成功
# tu[4][0] = 111
# print(tu)

# join(): 将序列中的元素, 以指定的字符连接生成一个新的字符串
# s = "alex"
# s1 = "sb".join(s)
# print(s1)

# 列表转字符串, 使用join方法
# 字符串转列表, 使用split方法
# li = ['taibai', 'alex', 'wusir', 'egon', '女神']
# s2 = "+++".join(li)


