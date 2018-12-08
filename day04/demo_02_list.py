li = ['alex', 'wusir', 'egon', '女神', 'taibai']

# 增加操作: append, insert
# append(元素)
# li.append("mike")
# print(li)

# insert(索引, 元素)
# 在索引前面插入元素
# li.insert(1, "cindy")

# 若传入大于列表的索引, 则插在列表的最后
# li.insert(100, "fzm")

# 若传入小于列表的索引(注意列表的倒序). 则插在列表的最前面
# li.insert(-100, "lx")
# print(li)


# 删除操作:  pop, remove, clear, del

# pop(): 默认弹出最后一个
# print(li.pop())

# pop(索引): 弹出索引位置的元素
# print(li.pop(0))

# remove(元素): 删去指定元素
# li.remove("alex")
# print(li)

# clear(): 清空列表
# li.clear()
# print(li) # []

# del: 可以切片删除, 可以直接删除列表
# del li
# print(li)   # NameError: name 'li' is not defined

# del li[1:-1:2]
# print(li)


# 修改操作
# li[0] = 'lx'
# print(li)

# li[0:2] = "fzmqweasdzxc"
li[0:2] = [1, 2, 3, '春哥', '咸鱼哥']
print(li)
