import requests
from hashlib import md5

class Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

from selenium import webdriver
from  time import sleep
from selenium.webdriver import ActionChains  #动作链
from PIL import Image
# 反检测
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#无头浏览器
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options)
bro.maximize_window()
bro.get('https://kyfw.12306.cn/otn/resources/login.html')

sleep(1)
# 登录账号
user_login = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
#账号密码
username = bro.find_element_by_id('J-userName')
password =bro.find_element_by_id('J-password')
username.send_keys('15777302660')
sleep(1)
password.send_keys('qq1986523538')
sleep(1)

# 验证码图片验证
# 将当前页面进行截图
sleep(2)         #延时等待响应到账号登录界面加载完成
bro.save_screenshot('aa.png')                   #.png,.jpg
# 确定验证码图片的左上角和右下角的坐标
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')                 #selector:#J-loginImg
data = code_img_ele.screenshot_as_png      #screenshot_png
# print(data)
with open('Code.jpg','wb') as fp :
    fp.write(data)

location = code_img_ele.location         #验证码图片左上角坐标
print(location)         #字典
size =code_img_ele.size                   #验证码的长(width)和宽(height)
print(size)             #字典
#确定左上角 和 右下角的坐标
rangle = (int(location['x']),int(location['y']),
          int(location['x'] + size['width']),int(location['y'] + size['height']))

#裁剪图片
i = Image.open('./aa.png')
code_img_name = './code.png'
frame = i.crop(rangle)  #指定裁剪区域
frame.save(code_img_name) #保存为xxx

# 使用超级鹰进行验证码识别
chaojiying = Client('qq1986523538', 'qq1986523538', '916463')
im = open('./Code.jpg', 'rb').read()
print(chaojiying.PostPic(im, 9004)['pic_str'])

result = chaojiying.PostPic(im, 9004)['pic_str']
#动作链鼠标点击选择图片
#处理获得的图片坐标
all_list = []         #存储被点击的点坐标 [[x1,y1] , [x2,y2]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)
#遍历列表，并用 动作链 实现对应坐标的点击动作
for l in all_list:
    x = l[0]
    y = l[1]
    #move_to_element_with_offset是为了将点击作用域的参照定位到验证码图片上
    ActionChains(bro).move_to_element_with_offset(code_img_ele,x,y).click().perform()
    sleep(0.5)

#点击登录
btn_login =bro.find_element_by_id('J-login')
btn_login.click()
sleep(1)
# 动作链 滑动验证
Slide_btn = bro.find_element_by_id('nc_1_n1z')  #定位滑块动作
action = ActionChains(bro)                #实例化动作
action.click_and_hold(Slide_btn)               #长按动作链                     #移动动作链
#每次向右移动34个像素点,总长340，perform()是立即执行
action.move_by_offset(340,0).perform()
sleep(0.5)
count = 0;
while bro.find_element_by_class_name('errloading'):
    bro.find_element_by_xpath('//*[@id="J-slide-passcode"]/div/span/a[1]').click()
    Slide_btn = bro.find_element_by_id('nc_1_n1z')  # 定位滑块动作
    action = ActionChains(bro)  # 实例化动作
    action.click_and_hold(Slide_btn)  # 长按动作链
     # 每次向右移动34个像素点,总长340，perform()是立即执行
    action.move_by_offset(340, 0).perform()
    sleep(0.5)
    count = count + 1
    if count == 5:
        print("sorry,遇到了无法解决的问题")
    break
    break
sleep(5)
bro.quit()