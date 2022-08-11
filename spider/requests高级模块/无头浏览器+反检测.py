from selenium import webdriver
from  time import sleep
#无头浏览
from selenium.webdriver.chrome.options import Options
#反检测
from selenium.webdriver import ChromeOptions

#无头浏览器
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#如何实现让selenium规避被检测的风险
#实现规避风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options)
# bro = webdriver.Chrome(executable_path='./chromedriver.exe')
#无可视化界面，无头浏览器   ， phantomJs(已经停止维护了)

bro.get('https://www.baidu.com')
print(bro.page_source)
sleep(2)
bro.quit()
