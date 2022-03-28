# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from bson.objectid import ObjectId


class CrawlSpaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = ObjectId()
    prdCate = scrapy.Field()
    prdTitle = scrapy.Field()
    prdImgUrl = scrapy.Field()
    prdImgLink = scrapy.Field()
    prdOriginPrice = scrapy.Field()
    prdSalePrice = scrapy.Field()
    prdDetailImgs = scrapy.Field()
    prdDetailThumbs = scrapy.Field()
    prdBrand = scrapy.Field()
    update = scrapy.Field()