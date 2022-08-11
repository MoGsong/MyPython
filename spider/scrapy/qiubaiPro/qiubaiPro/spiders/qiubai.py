import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # 终端储存
    # def parse(self, response):
    #     #解析作者的名称+内容
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     all_data = []
    #     for div in div_list:
    #         #xpath返回的是列表，且是Selector对象
    #         #extract()将Selector对象中的data参数提取出来
    #         #author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         # print(author,content)
    #
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #     return all_data

    # 管道储存
    def parse(self, response):
        # 解析作者的名称+内容
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        all_data = []
        for div in div_list:
            # xpath返回的是列表，且是Selector对象
            # extract()将Selector对象中的data参数提取出来
            # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()            #返回一个列表对象
            content = ''.join(content)                                           #列表转字符

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            yield item  # 将item提交给管道
