import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            #懒加载，伪属性，只有图片滑动到可视化区域时才会加载图片真正的src
            src = 'https:'+ div.xpath('./div/a/img/@src2').extract_first()
            # print(src)
            item = ImgsproItem()
            item['src'] = src
            yield item