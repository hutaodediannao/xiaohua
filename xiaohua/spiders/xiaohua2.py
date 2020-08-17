# -*- coding: utf-8 -*-
import scrapy
from ..items import XiaohuaItem


class Xiaohua2Spider(scrapy.Spider):
    name = 'xiaohua2'
    allowed_domains = ['xiaohua.zol.com.cn']
    start_urls = ['http://xiaohua.zol.com.cn/']

    def parse(self, response):
        jokes = response.xpath('//ul[@class="news-list video-list"]/li/a')
        # print('--------------------------------------------', len(jokes))
        for joke in jokes:
            item = XiaohuaItem()
            # 提取文本extract
            title = joke.xpath('./@title')[0].extract()
            href = 'http://xiaohua.zol.com.cn' + joke.xpath('./@href')[0].extract()
            item['title'] = title
            item['href'] = href
            print('-----------------', title, href)
            yield item
