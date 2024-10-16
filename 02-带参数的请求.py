import random
import re
import time

import requests

#
# class MaoYanSpider(object):
#     def __init__(self):
#         self.url = "https://www.maoyan.com/board/4?"
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
#             'Cookie': '__mta=48601881.1669894329016.1669989086764.1669989091647.38; uuid_n_v=v1; uuid=C86F9A70716B11ED8B7C3F15132DB86F938FA19CE80C408889429F6C12132955; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=184cd75521dc8-07cb15ffb328f7-26021151-1fa400-184cd75521ec8; _lxsdk=C86F9A70716B11ED8B7C3F15132DB86F938FA19CE80C408889429F6C12132955; __mta=48601881.1669894329016.1669899249182.1669902342726.8; _csrf=a1255b7c8212ceabdacf2e09ba413a76241155f1413d78700794962199e3da8a; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1669894329,1669982600; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1669989092; _lxsdk_s=184d2b83d09-5-c84-e5%7C%7C42'
#         }
#         self.params = {
#             "offset": 0
#         }
#
#     def get_html(self, url):
#         """发送请求功能"""
#         response = requests.get(url, headers=self.headers, params=self.params)
#         return response.text
#
#     def parse_html(self, html):
#         """提取数据"""
#         r_list = re.findall(
#             '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
#             html, re.S)
#         self.save(r_list)
#
#     def save(self, datas):
#         """存储数据"""
#         for data in datas:
#             li = [
#                 data[0].strip(),
#                 data[1].strip(),
#                 data[2].strip(),
#             ]
#             print(li)
#
#     def crawl(self):
#         """程序的入口"""
#         for offset in range(0, 91, 10):
#             self.params["offset"] = offset
#             html = self.get_html(url=self.url)
#             self.parse_html(html)
#             time.sleep(random.randint(1, 3))
#
#
# spider = MaoYanSpider()
# spider.crawl()
# https://search.jd.com/Search?
# keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&
# suggest=1.def.0.SAK7|MIXTAG_SAK7R,SAK7_M_AM_L5361,SAK7_M_COL_R,SAK7_M_ptrc_L23688,SAK7_S_AM_R,SAK7_D_HSP_R,SAK7_SC_PD_R,SAK7_SM_PB_R,SAK7_SM_PRK_R,SAK7_SM_PRC_R,SAK7_SM_PRR_R,SAK7_SS_PM_R,tsabtest_base64_U2VhcmNobGlzdF80MzkyfG1pZGRsZUhhdmU_tsabtest,SAK7_CS_PRF_R|&wq=shouji&pvid=37da9b1812ab4552ac63d4f35bf6a7eb
#
url = "https://www.maoyan.com/board/4?"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Cookie': '__mta=48601881.1669894329016.1669989097603.1670244870034.40; uuid_n_v=v1; uuid=C86F9A70716B11ED8B7C3F15132DB86F938FA19CE80C408889429F6C12132955; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=184cd75521dc8-07cb15ffb328f7-26021151-1fa400-184cd75521ec8; _lxsdk=C86F9A70716B11ED8B7C3F15132DB86F938FA19CE80C408889429F6C12132955; __mta=48601881.1669894329016.1669899249182.1669902342726.8; _csrf=0ae6da9af482d1c4e704cb3dd8daef800857ac8398a655dcce19e0e3338f1c35; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1669894329,1669982600,1670244870; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1670244870; _lxsdk_s=184e25a274f-1b8-86e-40c%7C%7C2'
}

canshu = {
    "offset": 0
}

for offset in range(0, 91, 10):
    canshu["offset"] = offset
    response = requests.get(url, headers=headers, params=canshu)
    print(response.url)
