import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'https://pic.netbian.com/tupian/25331.html'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    #content返回二进制属性数据
    page_text = requests.get(url=url,headers=headers).text
    bs_list = BeautifulSoup(page_text,'lxml')

    src = bs_list.find('div',class_='photo-pic')
    #print(src.a.img['data-pic'])
    img_src = 'https://pic.netbian.com/'+ src.a.img['data-pic']
    img_name = src.a.img['alt'] + '.jpg'
    img_data = requests.get(url=img_src, headers=headers).content
    #print(img_data)

    img_name = img_name.encode('ISO-8859-1').decode('gbk')
    print(img_name)

    #img_data = requests.get(url=img_src, headers=headers).content
    #img_name = bs_list.find('.class a > alt')[0] + '.jpg'

    #img_name = img_name.encode('ISO-8859-1').decode('gbk')

    with open(img_name,'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！')