from unicodedata import category
import scrapy
from random import randrange
import datetime
import os
from ..items import CrawlSpaItem 
from playwright.async_api import async_playwright
from bson.objectid import ObjectId
import json 
from pymongo import MongoClient


class SpaoSpider(scrapy.Spider):
    client = MongoClient('mongodb+srv://beoomtrack:beoomtrack@cluster0.wouwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    name = 'spao'
    allowed_domains = ['spao.com']
    start_urls = ['https://spao.com']
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, './fakeuseragent.csv')
    f_read = open(file_path,'r', encoding='UTF-8')
    fake_useragents = f_read.readlines()
    f_read.close()

    custom_settings = dict(
        DEFAULT_REQUEST_HEADERS={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-agent' : fake_useragents[randrange(len(fake_useragents))] 
        },  
    )
    flag = {
        'spaocom_cat' : {
            'man_main_cat' : 'https://spao.com/product/list.html?cate_no=56',
            'wm_main_cat' : 'https://spao.com/product/list.html?cate_no=55',  
            'man_cat' : {
                'manouter' : 'https://spao.com/product/list.html?cate_no=75',
                'mantop' : 'https://spao.com/product/list.html?cate_no=77',
                'manbottom' : 'https://spao.com/product/list.html?cate_no=78',
                'manshoes' : 'https://spao.com/category/%EC%8B%A0%EB%B0%9C/193/',
                'manbag' : 'https://spao.com/category/%EA%B0%80%EB%B0%A9/192/'
            },
            'women_cat' : {
                'womenouter' : 'https://spao.com/product/list.html?cate_no=62',
                'womentop' : 'https://spao.com/product/list.html?cate_no=64',
                'womenbottom' : 'https://spao.com/product/list.html?cate_no=68',
                'womenshoes' : 'https://spao.com/category/%EC%8B%A0%EB%B0%9C/214/',
                'womenbag' : 'https://spao.com/category/%EA%B0%80%EB%B0%A9/69/'
            },
        },
        'spao_cate' :{
            "manouter": { 
                        "_id" : ObjectId("623eabf9fa4d75ce471b59a4"), 
                        "id" : 2, 
                        "name" : "manouter", 
                        "slug" : "manouter"
                        },
             "mantop": { 
                        "_id" : ObjectId("623eac06fa4d75ce471b59a6"), 
                        "id" : 3, 
                        "name" : "mantop", 
                        "slug" : "mantop"
                        },
            "manbottom":{ 
                        "_id" : ObjectId("623eac11fa4d75ce471b59a8"), 
                        "id" : 4, 
                        "name" : "manbottom", 
                        "slug" : "manbottom"
                        },
            "manshoes":{ 
                        "_id" : ObjectId("623eac1bfa4d75ce471b59aa"), 
                        "id" : 5, 
                        "name" : "manshoes", 
                        "slug" : "manshoes"
                        },
            "manbag":{ 
                        "_id" : ObjectId("623eac24fa4d75ce471b59ac"), 
                        "id" : 6, 
                        "name" : "manbag", 
                        "slug" : "manbag"
                    },
            "womenouter":{ 
                        "_id" : ObjectId("623eac3dfa4d75ce471b59ae"), 
                        "id" : 7, 
                        "name" : "womenouter", 
                        "slug" : "womenouter"
                    },
            "womenbag" :{ 
                        "_id" : ObjectId("623eac6bfa4d75ce471b59b1"), 
                        "id" : 8, 
                        "name" : "womenbag", 
                        "slug" : "womenbag"
                    },
            "womenbottom":{ 
                        "_id" : ObjectId("623eac74fa4d75ce471b59b3"), 
                        "id" : 9, 
                        "name" : "womenbottom", 
                        "slug" : "womenbottom"
                    },
            "womentop":{ 
                        "_id" : ObjectId("623eac7dfa4d75ce471b59b5"), 
                        "id" : 10, 
                        "name" : "womentop", 
                        "slug" : "womentop"
                    },
            "womenshoes":{ 
                        "_id" : ObjectId("623eac9bfa4d75ce471b59b7"), 
                        "id" : 11, 
                        "name" : "womenshoes", 
                        "slug" : "womenshoes"
                    }

        }
    }             
    
    # ?????? banner crawl ????????????
    # async def parse(self, response):
    #     async with async_playwright() as pw:
    #         browser = await pw.chromium.launch()
    #         page = await browser.new_page()
    #         await page.goto("https://spao.com")
    #         title = await page.title()
    #         return {"title": title}
 
    def parse(self, response):        
        yield scrapy.Request(url=self.flag['spaocom_cat']['man_main_cat'], 
                            callback = self.parse_man_cat, 
                            dont_filter = True)
    
        yield scrapy.Request(url=self.flag['spaocom_cat']['wm_main_cat'], 
                            callback = self.parse_women_cat, 
                            dont_filter = True)                    

    def parse_man_cat(self, response):
        for key, value in self.flag['spaocom_cat']['man_cat'].items() :
            yield scrapy.Request(url=value, callback=self.parse_items, meta={'prdCate' : key,'page' : 1}, dont_filter = True)

    def parse_women_cat(self, response):
        for key, value in self.flag['spaocom_cat']['women_cat'].items() :
            yield scrapy.Request(url=value, callback=self.parse_items, meta={'prdCate' : key,'page' : 1}, dont_filter = True) 
    
    def parse_items(self,response):
        today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') 
        prdImgLink = response.css('div.mcontent>div>div>ul.prdList>li>div>div>div.prdImg>a::attr(href)').getall()
        prdTitle = response.css('div.mcontent>div>div>ul.prdList>li>div>div>div.prdImg>a>img::attr(alt)').getall()
        prdImgUrl= response.css('div.mcontent>div>div>ul.prdList>li>div>div>div.prdImg>a>img::attr(src)').getall()
        prdSalePrice = [int(pSP.replace(',' , '')) for pSP in response.css('div.mcontent>div>div>ul.prdList>li>div>div.description>div>span.price ::text').getall()]
        prdOriginPrice = [int(pOP.replace(',' , '')) for pOP in response.css('div.mcontent>div>div>ul.prdList>li>div>div.description>div>span.custom ::text').getall()]
        if response.css('a.last::attr(href)').get() != '#none' :
            last_page = response.css('a.last::attr(href)').get().split('=')[-1]
        else :
            last_page = 1

        if response.meta['page'] <= 1 :
            for j in range(2,int(last_page)+1) :
                yield scrapy.Request(url=response.url+"&page={}".format(j), 
                                    callback=self.parse_items,
                                    meta={'prdCate' : response.meta['prdCate'] ,'page' : j},
                                    dont_filter=True)
            
        for i in range (0,len(prdImgLink)):
            item=CrawlSpaItem()
            
            item["update"] = today
            item["prdCate"] = {}
            item["prdCate"]["_id"] = self.flag['spao_cate'][response.meta['prdCate']]["_id"]
            item["prdImgLink"] = "https://spao.com"+prdImgLink[i]
            item["prdImgUrl"] = "https:"+prdImgUrl[i]
            item["prdTitle"] = prdTitle[i]
            item["prdOriginPrice"] = prdOriginPrice[i]
            item["prdSalePrice"] = prdSalePrice[i]
            item["prdBrand"] = 'SPAO'
            yield scrapy.Request(url=item["prdImgLink"],callback=self.parse_detail, meta ={'item':item}, dont_filter=True)
    
    def parse_detail(self, response) : 
        item = response.meta['item']
        item["prdDetailThumbs"] = []
        item["prdDetailImgs"] =[]
        for pDT in response.css('div.cboth.detailArea>div>ul>li>img::attr(src)').getall() :
            prdDetailThumb = {"detailThumb" : "http:"+pDT }
            item["prdDetailThumbs"].append(prdDetailThumb)

        for pDI in response.css('div.cont>p>img::attr(src)').getall() :
            if pDI[0] !='/' :
                prdDetailImg = {"detailImg" : pDI} 
            else : 
                prdDetailImg = {"detailImg" : "https://spao.com"+pDI}
            item["prdDetailImgs"].append(prdDetailImg) 
        

        
        db = self.client.ecommerce_mongodb.manproduct_product
        db.insert_one(dict(item))
        yield item
        