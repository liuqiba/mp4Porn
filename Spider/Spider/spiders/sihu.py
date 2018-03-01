# -*- coding: utf-8 -*-
__author__ = 'yutiansut'
import scrapy
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from Spider.items import SpiderItem
import pymongo

class SihuSpider(scrapy.Spider):
   # download_delay = 1  
    name = "sihu"
    #allowed_domains = ["https://tub99.com/"]
    #start_urls = ['https://www.27sihu.com/','https://www.480r.com/','https://tub99.com/']
    start_urls = ['https://www.1102f.com/']
    items = []
    def parse(self, response):
        sel = Selector(response)  
        item=SpiderItem();
        html=response.xpath('//a/@href').extract()
        
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["sihu"]
       
        for h in html:
            if h.endswith('mp4'):
                if (db['mp4'].find({"mp4":h}).count()==0):
                    item['mp4']=h;
                    print ('mp4:',h)
                    yield item
                    yield SpiderItem
                else:
                    print ('already in')

              #  print '``````````````get MP4``````````````````'
               # 
            else:
                
                url='https://www.1102f.com'+h
                print ('url',url)
                # print url
                item['html']=url;
                yield Request(url, callback=self.parse,dont_filter=True)
        #    print h
        




