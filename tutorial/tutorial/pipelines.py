# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo

class TextPipeline(object):
    def __init__(self):
        self.limit = 50
    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Missing Text')

class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod                           #标识为类方法,类方法可以直接使用类名调用，cls可以看做一个类对象
    def from_crawler(cls ,crawler):        #通过crawler参数获得全局配置中的每个配置信息（settings.py）
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):     #当Spider开启时被调用的方法
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__    #__class__获得对象的类，__name__获得类名
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()