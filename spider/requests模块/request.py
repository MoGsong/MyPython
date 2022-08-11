#!/usr/bin/env python
# -*- coding:utf-8-*-

import requests
if __name__ == "__main__":
    #step 1:指定url
    url = 'https://www.sogou.com/'  #sougou
    #step2 :发起请求,返回一个响应对象
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    # step3:获取响应数据
    # text是字符串类型数据
    page_text = response.text
    print(page_text)
    #step4:持久化数据
    with open('.sogou.html', 'w', encoding='utf-8') as fp:
       fp.write(page_text)
    print('爬取结束')