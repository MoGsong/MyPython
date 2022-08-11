#1.验证码识别，获取验证码图片文字数据
#2.发起post请求
#3.对响应数据进行持久化存储

import requests
from lxml import etree
from codeclass import Client
if __name__ == "__main__":
      headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
      }
      url = 'http://www.renren.com/SysHome.do'
      page_text = requests.get(url=url,headers=headers).text
      tree = etree.HTML(page_text)
      code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')  #火球动态验证码的图片属性url
      code_img_data = requests.get(url=code_img_src,headers=headers)
      with open('./code.jpg','wb') as fp:
          fp.write(code_img_data)
      #使用云打码平台
      #{pass}
	  chaojiying = Client('qq1986523538', 'qq1986523538', '915688')	#用户中心>>软件ID 生成一个替换 96001
	  im = open('./code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
	  print(chaojiying.PostPic(im, 1902))