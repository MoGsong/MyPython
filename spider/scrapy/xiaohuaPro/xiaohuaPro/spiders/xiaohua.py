import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['http://www.521609.com/meinvxiaohua/']
    start_urls = ['http://www.521609.com/tuku/mxxz/']
    url = 'http://www.521609.com/tuku/mxxz/index_%d.html'
    page_num = 2

    def parse(self, response):
        # print("开始...")
        # print(response)
        li_list = response.xpath('/html/body/section/section[3]/ul/li | /html/body/div[4]/div[3]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a/p/text() | ./a[2]/text()').extract_first()
            #img_name = li.xpath('./a/p/text()')[0].encode('ISO-8859-1').decode('utf-8')
            # img_src = li.xpath('')
            print(img_name)

        if self.page_num <= 29:
            new_url = format(self.url % self.page_num)  #%d等于%self.page_num即网站页数
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)

