# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# scraped data -> Item container -> JSON/CSV/XML
# scraped data -> Item container -> Pipeline -> SQL/Mongodb

# Need to uncomment Pipeline section in settings.py file otherwise this code wouldn't get called

# import sqlite3
# import mysql.connector
import pymongo

class QuotePipeline(object):

    def __init__(self):
        # self.create_connection()
        # self.create_table()

        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['myquotes']
        self.collection = db['quotes_tb']

    # def create_connection(self):
    #     # self.conn = sqlite3.connect('myquotes.db')
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         user = 'root',
    #         passwd = 'tiger',
    #         database = 'myquotes',
    #         port = 3307
    #     )
    #     self.curr = self.conn.cursor()
    #
    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
    #     self.curr.execute("""create table quotes_tb(
    #                     title text,
    #                     author text,
    #                     tag text
    #                     )""")

    def process_item(self, item, spider):
        # self.store_db(item)
        self.collection.insert(dict(item))
        return item


    # def store_db(self, item):
    #     # in sqlite3 placeholders are ?; whereas in mysql %s
    #     self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""", (
    #         item['title'][0],
    #         item['author'][0],
    #         item['tag'][0],
    #     ))
    #     self.conn.commit()