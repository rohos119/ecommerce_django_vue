import scrapy
from random import randrange
import datetime
import os
from ..items import CrawlSpaItem 
from playwright.async_api import async_playwright

class SpaoSpider(scrapy.Spider):
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
    }             
    
    # 동적 banner crawl 수정필요
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
        prdSalePrice = response.css('div.mcontent>div>div>ul.prdList>li>div>div.description>div>span.price ::text').getall()
        prdOriginPrice = response.css('div.mcontent>div>div>ul.prdList>li>div>div.description>div>span.custom ::text').getall()
        if response.css('a.last::attr(href)') :
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
            item['update'] = today
            item['prdCate'] = response.meta['prdCate']
            item['prdImgLink'] = 'https://spao.com'+prdImgLink[i]
            item['prdImgUrl'] = "https:"+prdImgUrl[i]
            item['prdTitle'] = prdTitle[i]
            item['prdOriginPrice'] = prdOriginPrice[i]
            item['prdSalePrice'] = prdSalePrice[i]
            yield scrapy.Request(url=item['prdImgLink'],callback=self.parse_detail, meta ={'item':item}, dont_filter=True)
    
    def parse_detail(self, response) : 
        item = response.meta['item']
        item['prdDetailThumb'] = response.css('div.cboth.detailArea>div>ul>li>img::attr(src)').getall()
        item['prdDetailImg'] = response.css('div.cont>p>img::attr(src)').getall()

        yield item
            