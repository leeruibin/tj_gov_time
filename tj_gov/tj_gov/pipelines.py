# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import GavAccItem,CheatItem,RelegateItem,DeadAccItem
import pymysql
class TjGovPipeline(object):
    # 后期连接数据库
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    password='',
                                    db='tianjin',
                                    charset='utf8')

    def close_spder(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        ##可以分别打开不同的文件，不同的实例放到不同文件中去
        ##或者连接数据库直接操作数据库
        self.conn.commit()
        if isinstance(item,GavAccItem):
            try:
                cur = self.conn.cursor()
                sql = 'INSERT INTO accident VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

                cur.execute(sql,(item['type'],
                                 item['code'],
                                 item['accName'],
                                 item['peoName'],
                                 item['carType'],
                                 item['carNumber'],
                                 item['result'],
                                 item['date']))
            except Exception:
                print("Mysql error")
            self.conn.commit()

        elif isinstance(item,CheatItem):
            pass
        elif isinstance(item,RelegateItem):
            try:
                cur = self.conn.cursor()
                sql = 'INSERT INTO relegate VALUES (%s,%s,%s,%s,%s,%s)'

                cur.execute(sql,(item['type'],
                                 item['name'],
                                 item['peoName'],
                                 item['result'],
                                 item['department'],
                                 item['date']))
            except Exception:
                print("Mysql error")
            self.conn.commit()

        elif isinstance(item,DeadAccItem):
            try:
                cur = self.conn.cursor()
                sql = 'INSERT INTO dead VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

                cur.execute(sql,(item['type'],
                                 item['code'],
                                 item['accName'],
                                 item['peoName'],
                                 item['carType'],
                                 item['carNumber'],
                                 item['department'],
                                 item['date']))
            except Exception:
                print("Mysql error")
            self.conn.commit()



