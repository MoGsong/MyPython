import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=62095104_43_oem_dg&wd=ip']
    start_urls = ['https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=62095104_43_oem_dg&wd=ip']

    def parse(self, response):
       page_text = response.text()
       with open('ip.html','w',encoding='utf-8') as fp:
           fp.write(page_text)
