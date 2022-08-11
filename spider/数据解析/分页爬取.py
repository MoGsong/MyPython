import requests
import re
import os
if __name__ == "__main__":
    #创建一个文件夹，保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.makedirs('./qiutuLibs')
    headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
    #设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/2/'
        #pageNumb = 2
    for pageNumb in range(1,5):
        new_url = format(url%pageNumb)

        page_text = requests.get(url=new_url,headers=headers).text
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'   #正则匹配的图片目录
        img_src_list = re.findall(ex,page_text,re.S)
         #print(img_src_list)
        for src in img_src_list:
            src = 'https:'+ src                   #拼接一个完整图片url
            img_date = requests.get(url=src,headers=headers).content
            #生成图片名称
            img_name = src.split('/')[-1]
            imgPath ='qiutuLibs/' + img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_date)
                print(img_name,'下载成功!')