import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件名：源文件的唯一标识
    name = 'first'
    #允许的域名：限定start_urls列表中那些url可以进行请求发送 通常不用
    #allowed_domains = ['www.baidu.com']
    #起始的url:该列表中存放的url会被scrapy自动进行请求发送
    start_urls = ['http://www.baidu.com/','https://www.sogou.com']

    #数据解析
    def parse(self, response):
        pass
