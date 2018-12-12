"""
    re模块的优先级问题
        1. findall()优先级: ?:
        2. split()优先级: ()

"""
import re


# 返回结果: ['sogou']
# 这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,需要用?:去掉优先级
res = re.findall("www.(baidu|sogou).com", "www.sogou.com")
print(res)

# 返回结果['www.sogou.com']
# 使用?:去掉优先级
res2 = re.findall("www.(?:baidu|sogou).com", "www.sogou.com")
print(res2)


# 返回结果: ['qwe', '', '', 'zxc']
# 因为split默认会去掉匹配到的字符串, 如果想要保留结果, 需要用()去掉优先级
res3 = re.split("\d", "qwe345zxc")
print(res3)

# 返回结果: ['qwe', '3', '', '4', '', '5', 'zxc']
# 使用()去掉优先级
res4 = re.split("(\d)", "qwe345zxc")
print(res4)




