# -*- coding: utf-8 -*-
import requests                                    #爬取本草纲目
from bs4 import BeautifulSoup       #导入包
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'http://www.gushicimingju.com/dianji/bencaogangmu/'
      page_text = requests.get(url=url,headers=headers).text
      soup = BeautifulSoup(page_text, 'lxml')
      print(soup.select('.main-content > ul > li'))
      li_list = soup.select('.main-content > ul > li')                    #所有li标签
      print('--------li_list-----------',li_list[0])

      fp = open('./bencaogang.txt','w',encoding='utf-8')
      for li in li_list[:]:                                #从列表中提取li
            title = li.string
            #print(title)
            try:                                                             #toubu没有url所以要捕获异常
                  detail_url = 'http://www.gushicimingju.com' + li.a['href']
                  #print(detail_url)#章节标题和详情页
                  #对详情页发起请求，解析章节内容

                  detail_url_text = requests.get(url=detail_url,headers=headers).text
                  #解析出详情页中的内容
                  detail_soup = BeautifulSoup(detail_url_text,'lxml')                #zaishilixiangqingyeduixiang

                  div_tag = detail_soup.find('div',class_='shici-content check-more')
                  content = div_tag.text
                  fp.write(title +':'+content+'\n')
                  print(title,'爬取成功！')
            except:
                  fp.write(title)