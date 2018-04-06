import scrapy

class SpiderTest(scrapy.Spider):
    name = 'Stest'
    allowed_domains = ['hupu.com']
    start_urls = ['https://soccer.hupu.com/england/',
    'https://soccer.hupu.com/spain/'
    ]

    def parse(self,response):
        filename = response.url.split('/')[-2]+'.html'
        with open(filename,'wb') as f:
            f.write(response.body)