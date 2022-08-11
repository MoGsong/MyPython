import os
import requests
from lxml import etree
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'https://pic.netbian.com/4kmeinv/'
      page_text = requests.get(url=url, headers=headers).text
      #response = requests.get(url=url, headers=headers)
      #response.encoding = 'utf-8'                              #img_name乱码，手动编码（失败）
      #page_text = response.text

      tree = etree.HTML(page_text)
      #解析 src的属性 和 alt的属性

      if not os.path.exists('./picLibs'):
            os.makedirs('./picLibs')
      li_list = tree.xpath('//div[@class = "slist"]/ul/li')
      for li in li_list:
            img_src ='https://pic.netbian.com/'+li.xpath('./a/img/@src')[0]
            img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
            img_name = img_name.encode('ISO-8859-1').decode('gbk')
            #通用处理中文乱码的解决方案
            #print(img_name,img_src)
            #进行图片持久化存储
            # print(img_src)
            img_data = requests.get(url=img_src,headers=headers).content
            #print(img_data)
            img_path = 'picLibs/' + img_name
            with open(img_path,'wb')as fp:
                 fp.write(img_data)
                 print(img_name,'下载成功！！')

