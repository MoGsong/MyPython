from selenium import webdriver
from lxml import etree
#实例化一个浏览器对象，传入浏览器的驱动程序
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
#bro.get('http://125.35.6.84:81/xk/')
bro.get('www.baidu.com/')
page_text = bro.page_source

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id = "id="s-top-left""]/li')
for li in li_list:
    name =li.xpath('./dl/@title')[0]
    print(name)
bro.quit()