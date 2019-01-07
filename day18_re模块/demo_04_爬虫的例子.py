import re
from urllib.request import urlopen


def get_page(url):
    response = urlopen(url)
    return response.read().decode("utf-8")


def parse_page(s):
    ret = re.findall(
        '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', s, re.S)
    return ret


def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = get_page(url)
    ret = parse_page(response_html)
    return ret


count = 0
for i in range(5):
    ret = main(count)
    # 将爬取到的电影排名, 写入到文件里
    with open("movie.txt", "a", encoding="utf-8") as f1:
        f1.write(str(ret))
    count += 25


