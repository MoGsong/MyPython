import requests
import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'

    # allowed_domains = ['https://www.zhipin.com/c101010100/?ka=open_joblist']
    start_urls = ['https://www.zhipin.com/c101010100/?page=2&ka=open_joblist']

    # 尝试下使用代理IP处理302,配置中配置
    def start_requests(self,dont_filter=True):
        for i in self.start_urls:
            yield scrapy.Request(url=i, meta={
                'dont_redirect': True,  # 这个可以
                'handle_httpstatus_list': [301,302]  # 这个不行
            }, callback=self.parse)
    # scrapy.Request(''.join(start_urls),dont_filter=True, cookies=None)
    url = 'https://www.zhipin.com/c101010100/?page=2&ka=page-%d'
    num = 2

    # 回调函数接收 传 参
    def parse_detail(self,response):
        item = response.meta['item']
        job_dsec = response.xpath('//*[@id="main"]/div[2]/div/div[2]/div[2]/div[1]/div//text()').extract_first()
        job_dsec = ''.join(job_dsec)
        # print(job_dsec)
        item['job_dsec'] = job_dsec
        yield item             #提交给管道

    #shouye
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        for li in li_list:
            item = BossproItem()

            job_name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/text()').extract_first()
            # print(job_name)
            item['job_name'] = job_name
            detail_url = 'https://www.zhipin.com/' + li.xpath('./div/div[1]/div[1]/div/@href').extract_first()
            # print(detail_url)
            #请求传参：meta作为一个字典传递给对应的回调函数
            yield scrapy.Request(detail_url,dont_filter=True,callback=self.parse_detail,meta={'item':item})

            #分页操作
            if self.num <= 3:
                new_url = format(self.url%self.num)
                self.num += 1

                yield scrapy.Request(new_url,callback=self.parse)

