# 实例化etree对象，将被解析的页面源码加载到该对象
# etree.parse(filePath)  本地获取
# etree.HTML('page_text') 互联网获取
# xpath('xpath表达式')  就可以调用xpath方法   返回列表[]
# '/'表示从根节点开始定位，表示一个层级 ，  ‘//’表示多个层级  , //div[@class = "**"] 属性定位，索引定位//div[@class = "song"]/p[index]
# 调用etree的xpath方法结合表达式对标签定位和内容的捕获
#'//div[@class = "tang"]//li[5]/a/text()' houjia [0] libiaobianwenbenzifu       若不是直系文本改用//text
#tree.xpath('//div[@class = "song"]/img/@src') 取图片属性    取属性表达式  /@attr        title = li.xpath('./div[2]/h2/a/text()')[0]
# -*- coding: utf-8 -*-
import requests
from lxml import etree     #daoru etree
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'https://pic.netbian.com/tupian/27019.html'
      """img_data = requests.get(url=url, headers=headers).content
      with open('.jpg', 'wb') as fp:
            fp.write(img_data)"""

