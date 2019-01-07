# 1.用map来处理字符串列表,把列表中所有人都变成nb,比方alex_nb
# names = ['mike', 'cindy', 'xiaoma', 'jack']
#
# def change_name(name):
#     return name + "_nb"
#
# names2 = map(change_name, names)
# for i in names2:
#     print(i)

# 2.用filter函数处理数字列表, 将列表中所有的偶数筛选出来
nums = [1, 3, 5, 6, 7, 8]


# 方法1: 列表推导式
# nums2 = [i for i in nums if i % 2 == 0]
# print(nums2)

# 方法2: filiter
# def get_even(num):
#     return num % 2 == 0
#
# nums2 = filter(get_even, nums)
# for i in nums2:
#     print(i)
