import re

import requests
"""
对于requests模块的安装：我明明安装了 但是为什么在我的pycharm里面使用不了
这个是因为 
1-你们在pycharm里面使用了虚拟环境
2-你的电脑有多个python的环境但是你在pycharm指定的解释器和你下载模块用的解释器不一样
"""


class DouBanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        # self.headers 字典   {"1"}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

    def get_html(self, url):
        """发送请求功能"""
        # requests帮我们发送请求 发送是一个get请求
        response = requests.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html):
        """提取数据"""
        r_list = re.findall('<span class="title">(.*?)</span>.*?<p class="">(.*?)</p>', html, re.S)
        self.save(r_list)

    def save(self, datas):
        """存储数据"""
        for data in datas:
            name = data[0]
            infos = data[1].strip().replace("&nbsp;", "").split("<br>")
            types = infos[1]
            content = infos[0]
            r_list = re.findall('导演: (.*?)主演: (.*?)\.', content)
            if not r_list:
                r_list = re.findall('导演: (.*?)主(.*?)\.', content)
            print(name)
            print("导演", r_list[0][0])
            print("主演", r_list[0][1])
            print("年份/类型", types.strip())
            print()

    def crawl(self):
        """程序的入口"""
        html = self.get_html(self.url)
        self.parse_html(html)


spider = DouBanSpider()
spider.crawl()
