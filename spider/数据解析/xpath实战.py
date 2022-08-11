#爬取58-二手房的房源信息
# -*- coding: utf-8 -*-
import requests
from lxml import etree     #daoru etree
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'https://bj.58.com/ershoufang'                     #wangzhanbiangeng
      page_text = requests.get(url=url,headers=headers).text

      tree = etree.HTML(page_text)

      fp = open('58.txt','w',encoding='utf-8')
      li_list = tree.xpath('//ul[@class = "hourse-list-wrap"]/li')
      for li in li_list:
            title = li.xpath('./div[2]/h2/a/text()')[0]          #加‘.’，不然会从根节点开始解析
            print(title)
            fp.write(title+'\n')