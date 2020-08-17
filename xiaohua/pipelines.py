# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiaohuaPipeline(object):

    def open_spider(self, spider):
        self.fp = open('./xiaohua.txt', mode='a',encoding='utf-8')

    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        self.fp.write('%s, %s\n'%(item['title'], item['href']))
        return item
