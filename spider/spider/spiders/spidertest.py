import scrapy
from spider.items import SpiderItem

class SpiderTest(scrapy.Spider):
    name = 'Stest'
    allowed_domains = ['bbs.hupu.com']
    start_urls = ['https://bbs.hupu.com/'
    ]

    def parse(self,response):
        for href in response.css(''):
            url = response.urljoin(response.url,href.extract())
            yield scrapy.Request(url,callback=self.parse_clubs)

    
    def parse_clubs(self,response):
        for sel in response.xpath('//head'):
            item = SpiderItem()
            item['title']=sel.xpath('title/text()').extract()
            #item['link']=sel.xpath().extract()
            #item['desc']=sel.xpath().extract()
            yield item