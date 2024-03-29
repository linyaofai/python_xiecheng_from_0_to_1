# -*- coding:utf-8 -*-
import requests
from time import time
'''小梁不禁暗想：是我的程序写的太挫了吗？会不会是lxml这个库解析的速度太慢了，用正则表达式会不会好一些？

于是小梁把lxml库换成了标准的re库。'''
import re
url = 'https://movie.douban.com/top250'


def fetch_page(url):
    response = requests.get(url)
    return response


def parse(url):
    response = fetch_page(url)
    page = response.content

    fetch_list = set()
    result = []

    for title in re.findall(rb'<a href=.*\s.*<span class="title">(.*)</span>', page):
        result.append(title)

    for postfix in re.findall(rb'<a href="(\?start=.*?)"', page):
        fetch_list.add(url + postfix.decode())

    for url in fetch_list:
        response = fetch_page(url)
        page = response.content
        for title in re.findall(rb'<a href=.*\s.*<span class="title">(.*)</span>', page):
            result.append(title)

    for i, title in enumerate(result, 1):
        title = title.decode()
        # print(i, title)
def main():
    from time import time
    start = time()
    for i in range(5):
        parse(url)
    end = time()
    print('Cost {} seconds'.format((end - start) / 5))

if __name__ == '__main__':
    main()