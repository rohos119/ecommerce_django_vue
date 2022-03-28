import pymongo
import datetime

class EcommerceCrawl1Pipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'mongodb+srv://beoomtrack:beoomtrack@cluster0.wouwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        )
        db = self.conn['ecommerce_mongobd']
        self.collection = db['seller_db']


    def process_item(self, item, spider):
        self.collection.save(dict(item))
        return item

    def close_spider(self, spider):
        body = spider.crawler.stats.get_stats()
        body['end_time'] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.collection3.insert(body)
