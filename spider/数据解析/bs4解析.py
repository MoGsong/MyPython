# -*- coding: utf-8 -*-
import requests                      #本草纲目
from bs4 import BeautifulSoup       #导入包
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'http://www.gushicimingju.com/dianji/bencaogangmu/'
      page_text = requests.get(url=url,headers=headers).text
      soup = BeautifulSoup(page_text,'lxml')
      print(soup.div)
      print(soup.a)
      #print(soup.contents)
      print(soup.find('a'))

      print('------------')
      print(soup.select('.main-content > ul li'))                    #得到所有目录标签，是一个list
      print(soup.find_all('li'))
      li = soup.find_all('li')

      li_list = soup.select('.main-content > ul > li')
      print(li_list)
      print('____________')
      #print(soup.find('div', class_='main-content'))
      print(soup.find('ul',class_='content-left left-2-col'))

      print(soup.select('.main-content > ul > li a')[0]['href'])
      new_url = 'http://www.gushicimingju.com' + soup.select('.main-content > ul > li a')[0]['href']

      detail_url_text = requests.get(url=new_url, headers=headers).text
      detail_soup = BeautifulSoup(detail_url_text, 'lxml')                               #实例化详情页的BS4对象

      div_tag = detail_soup.find('div', class_='shici-content check-more')        #定位文本内容
      print(div_tag.contents)
      print('==========')
      print(div_tag.text)                                                         #打印文本内容

      """fp = open('./bencaogang.txt', 'w', encoding='utf-8')
      for li in li_list:
            title = li.a.string
            detail_url = 'www.gushicimingju.com'+li.a['href']
            print(detail_url)#章节标题和详情页
            #对详情页发起请求，解析章节内容
            detail_url_text = requests.get(url=detail_url,headers=headers).text
            #解析出详情页中的内容
            detail_soup = BeautifulSoup(detail_url_text,'lxml')                #zaishilixiangqingyeduixiang
            div_tag = detail_soup.find('div',class_='shici-content check-more')
            content = div_tag.text
            fp.write(title +':'+content+'\n')
            print(title,'爬取成功！')"""



      #实例化bs对象，将本地或互联网上的数据加载到该对象中
      #fp = open('./bencao.html','r',encoding='utf-8')         #打开本地文件
      #soup = BeautifulSoup(fp,'lxml')                         #返回一个实例化好的该对象
#分析方法和属性
      #print(soup)  soup.tagName 返回html中第一次出现的标签。 print(soup.a)   直接定位（）首个
      #soup.find('tagName')                              与soup.tagName等价
      #soup.find('div',class_attr='song')                属性定位，class后面加下划线表示参数，否则表示关键字
      #soup.findall()                                    返回的是符合要求的所有标签（列表）
      #soup.select('.class > ul > li > a')[0]   '.'是选择器，选择属性 >表示逐层选择，[numb]列表序号
      #soup.select('.class > ul > li  a')[0]    '空各'表示多个层级
#获取标签之间的文本数据：
      #soup.a.text/string/get_text()    text/get_text获取标签中所有的文本内容   string获取标签直系的文本内容
      #属性值：soup.a['href']   获得的是href属性值