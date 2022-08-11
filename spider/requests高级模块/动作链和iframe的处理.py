from selenium import webdriver
from  time import sleep
#导入动作链
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# 如果定位的标签存在iframe标签纸中的，则需进行如下操作才可以进行定位
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult') # 切换浏览前标签的定位作用域
div = bro.find_element_by_id('draggable')


# 动作链
action = ActionChains(bro)
#点击长按
action.click_and_hold(div)

for i in range(5):
    #每次向右移动17个像素点，perform()是立即执行
    action.move_by_offset(17,0).perform()
    sleep(0.3)

#释放动作链
action.release()
bro.quit()

