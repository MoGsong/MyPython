"""import requests
from lxml import etree
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'https://www.aqistudy.cn/historydata/'                           #爬取全国城市名称
      page_text = requests.get(url=url,headers=headers).text
      tree = etree.HTML(page_text)
      host_li_list = tree.xpath('//div[@class = "bottom"]/ul/li')
      all_city_name = []
      for li in host_li_list:
            hot_city_name = li.xpath('./a/text()')[0]
            all_city_name.append(hot_city_name)                              #热门城市

      city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
      for li in city_name_list:
            city_name = li.xpath('./a/text()')[0]
            all_city_name.append(city_name)                                  #全部城市

      print(all_city_name,len(all_city_name))"""
import requests
from lxml import etree
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'https://www.aqistudy.cn/historydata/'                           #爬取全国城市名称
      page_text = requests.get(url=url,headers=headers).text
      tree = etree.HTML(page_text)
      #解析到热门城市对应的a标签
      #//div[@class = "bottom"]/ul/li/a        热门城市的层级关系
      #//div[@class="bottom"]/ul/div[2]/li    全部城市的层级关系
      a_list = tree.xpath('//div[@class = "bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a') #按位或
      all_city_name = []
      for a in a_list:
            city_name = a.xpath('./text()')
            all_city_name.append(city_name)
      print(all_city_name, len(all_city_name))