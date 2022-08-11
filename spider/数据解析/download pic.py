import requests
if __name__ == "__main__":
    url = 'https://pic.netbian.com//uploads/allimg/200102/193708-15779650288588.jpg'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    #content返回二进制属性数据
    pic_data = requests.get(url=url,headers=headers).content
    name = '0' +'.jpg'
    with open(name,'wb') as fp:
            fp.write(pic_data)
            print(name, '下载成功！！')