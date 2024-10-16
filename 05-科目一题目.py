import requests
from lxml import etree


class JsyKsSpider(object):
    def __init__(self):
        self.url = "https://www.jsyks.com/kmy-mnks"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }

    def get_html(self, url):
        """发送请求功能"""
        response = requests.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html):
        """提取数据"""
        html = etree.HTML(html)
        lis = html.xpath('//ul[@class="Content"]/li')
        for li in lis:
            # 题目
            title = li.xpath('./strong/text()')[0]
            # 选项
            option = li.xpath('./b/text()')
            # 答案
            k = li.xpath('./@k')[0]
            if k == 'R':
                k = "正确"
            elif k == "E":
                k = "错误"

            # 有的题目是有图片的
            img_url = li.xpath('./strong/u/img/@src')
            if img_url:
                img_url = f"https:{img_url[0]}"
            else:
                img_url = None

            print(title)
            print(option)
            print(k)
            print(img_url)
            print()

    def save(self):
        """存储数据"""
        pass

    def crawl(self):
        """程序的入口"""
        html = self.get_html(url=self.url)
        self.parse_html(html)


spider = JsyKsSpider()
spider.crawl()
