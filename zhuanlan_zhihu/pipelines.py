#!user/bin/env python3
# -*- coding: utf-8 -*-
import pymongo
from .items import UserItem,QuestionItem,AnswerItem,ArticleItem
#import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

##当Item在Spider中被收集之后，它将会被传递到Item Pipeline
##每个Item Pipeline组件接收到Item,定义一些操作行为，比如决定此Item是丢弃而存储。
##以下是item pipeline的一些典型应用：
##验证爬取的数据(检查item包含某些字段，比如说name字段)
##查重(并丢弃)
##将爬取结果保存到文件或者数据库中
##编写item pipeline很简单，item pipiline组件是一个独立的Python类，必须实现process_item方法:

class MysqlPipeline(object):
    def __init__(self):
        self.count=1
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    collection_name = 'user'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_HOST'),
            mongo_db=crawler.settings.get('MONGO_DATABASE','zhihu')
        )

    def open_spider(self, spider):##当spider被开启时，这个方法被调用
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):##当spider被关闭时，这个方法被调用
        self.client.close()

    def process_item(self, item, spider):##当Item在Spider中被收集之后，都需要调用该方法
        primary="id"
        collection=""
        if isinstance(item,UserItem):
            collection="user"
            primary="url_token"            
        elif isinstance(item,QuestionItem):
            collection="question"
        elif isinstance(item,AnswerItem):
            collection="answer"
        elif isinstance(item,ArticleItemItem):
            collection="article"
        else:
            print("process_item:save %s exception" % collection)
            return item
        ###这里以每个用户url_token为ID，有则更新，没有则插入
        if dict(item)=={}:
            print("empty item")
            return item        
        try:
            self.db[collection].update({primary: item[primary]}, {'$set': dict(item)}, True)
            print("process_item save ok: collection,%s ;primary,%s" %(collection,primary))
            return item
        except Exception :
            print("process_item save exception: collection,%s ;primary,%s" %(collection,primary))
            ##print(item)
            return item
    
    
    
    '''
    为了启用Item Pipeline组件，必须将它的类添加到 settings.py文件ITEM_PIPELINES 配置，就像下面这个例子:
    ITEM_PIPELINES = {
        #'tutorial.pipelines.PricePipeline': 100,
        'zhihuuser.pipelines.MongoPipeline': 300,
    }
    分配给每个类的整型值，确定了他们运行的顺序，item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内。
    
    
    settings里面要加上两行才能跑
    MONGO_URI = 'localhost'
    MONGO_DATABASE = 数据库名'zhihu'
    '''