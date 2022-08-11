from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
# 快捷登录
# user = bro.find_element_by_id('img_out_1986523538')
# user.click()

# 账号密码登录
log_page = bro.find_element_by_id('switcher_plogin')
log_page.click()
user = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')
user.send_keys('1070962214')
sleep(2)
password.send_keys('SHEisWDS1399')
sleep(1)
login_btn = bro.find_element_by_id('login_button')
login_btn.click()
# sleep(3)
# bro.quit()





# #登录空间爬取数据
# import requests
# from selenium import webdriver
# from lxml import etree
# import time
#
# driver = webdriver.Chrome(executable_path='./chromedriver.exe')
# driver.get('https://qzone.qq.com/')
# #在web 应用中经常会遇到frame 嵌套页面的应用，使用WebDriver 每次只能在一个页面上识别元素，对于frame 嵌套内的页面上的元素，直接定位是定位是定位不到的。这个时候就需要通过switch_to_frame()方法将当前定位的主体切换了frame 里。
# driver.switch_to.frame('login_frame')
# driver.find_element_by_id('switcher_plogin').click()
#
# #driver.find_element_by_id('u').clear()
# driver.find_element_by_id('u').send_keys('1070962214')  #这里填写你的QQ号
# #driver.find_element_by_id('p').clear()
# driver.find_element_by_id('p').send_keys('SHEisWDS1399')  #这里填写你的QQ密码
#
# driver.find_element_by_id('login_button').click()
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# time.sleep(2)
# page_text = driver.page_source
#
# tree = etree.HTML(page_text)
# #执行解析操作
# li_list = tree.xpath('//ul[@id="feed_friend_list"]/li')
# for li in li_list:
#     text_list = li.xpath('.//div[@class="f-info"]//text()|.//div[@class="f-info qz_info_cut"]//text()')
#     text = ''.join(text_list)
#     print(text+'\n\n\n')
#
# driver.close()