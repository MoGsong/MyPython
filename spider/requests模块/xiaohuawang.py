import requests
from lxml import etree
if __name__ == "__main__":
    #step 1:指定url
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    url = 'http://m.521609.com/tuku/mxxz/'
    #step2 :发起请求,返回一个响应对象
    res = requests.get(url=url,headers=headers)
    # step3:获取响应数据
    # text是字符串类型数据
    page_text = res.text
    response = etree.HTML(page_text)
    li_list = response.xpath('/html/body/section/section[3]/ul/li')
    #/html/body/div[4]/div[3]/ul/li
    #/html/body/section/section[3]/ul/li
    #重写父类的方式写文件，发现不行 -_-
    # fp = None
    # def open_fp(self, spider):
    #     self.fp = open('xiaohua.txt', 'w', encoding='utf-8')
    #
    # def process_li(self,li_list,spider):
    #     for li in li_list:
    #         img_name = li.xpath('./a/p/text()')[0].encode('ISO-8859-1').decode('utf-8')
    #         #img_name = ''.join(img_name)                #列表转字符
    #         # img_name = img_name.encode('ISO-8859-1').decode('gbk')
    #         print(img_name)
    #         # print(page_text)
    #         # fp.write(page_text)
    #         fp.write(img_name + '\n')
    #
    # def close_fp(self, spider):
    #     self.fp.close()
    for li in li_list:
        img_name = li.xpath('./a/p/text()')[0].encode('ISO-8859-1').decode('utf-8')
        #img_name = ''.join(img_name)                #列表转字符
        # img_name = img_name.encode('ISO-8859-1').decode('gbk')
        print(img_name)
        # print(page_text)
        # fp.write(page_text)
        with open('xiaohua.txt', 'a', encoding='utf-8') as fp:
            fp.write(img_name + '\n')
    print('爬取结束')
