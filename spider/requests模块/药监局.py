#爬取药监局生产许可，只能爬取页面，不能访问动态数据
import requests
if __name__ == "__main__":
    url = 'https://125.35.6.84:81/xk/'   #药监网址变更了
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text

    with open('xxx.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
