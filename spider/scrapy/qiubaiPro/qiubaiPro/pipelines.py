# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiproPipeline:
    fp = None
    #重写父类方法：该方法只会在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('starting..')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')

    #处理item对象
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' +content + '\n')

        return item     #会被传递给下一个被执行的管道类
    def close_spider(self,spider):
        print('over!')
        self.fp.close()

 #管道文件对应将一组数据储存到一个平台或载体中
# class mysqlPipeline(object):
#     conn = None
#     cursor = None
#     def open_spider(self,spider):
#         self.conn = pymysql.Connect(host= '192.168.58.1',port=3306,user='root',passwd='123456',db='qiubai',charset='utf8')
#         self.conn.sql = "CREATE DATABASE IF NOT EXISTS qiubai"
#         self.conn.cursor.execute(self.conn.sql)
#         # self.conn.cursor().execute('create database qiubai')
#         # self.conn.cursor().execute('create table qiubai.item (...)')
#     def process_item(self,item,spider):
#         self.cursor = self.conn.cursor()
#         try:
#             self.cursor.execute('insert into qiubai value("%s","%s")'%(item["author"],item["content"]))
#             self.conn.commit()
#         except Exception as e:
#             print(e)
#             self.conn.rollback()
#             return item
#     def close_spider(self,spider):
#         self.cursor.close()
#         self.conn.close()