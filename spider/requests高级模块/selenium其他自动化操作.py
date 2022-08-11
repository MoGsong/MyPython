from selenium import webdriver
from lxml import etree
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.taobao.com/')
search_input = bro.find_element_by_id('q') #定位搜索框
search_input.send_keys('Iphone')
#执行js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
btn = bro.find_element_by_class_name('btn-search') #搜索按钮
btn.click()

# bro.get('https://www.baidu.com')
# sleep(2)
# bro.back()            #回退
# sleep(2)
# bro.forward()

sleep(3)
bro.quit()
