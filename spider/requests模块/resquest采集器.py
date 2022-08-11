#UA检测:USER-AGENT  门户网张服务器会检测对应请求 载体身份标识，如果为某一浏览器说明是正常请求
#否则为不正常请求（爬虫），服务器可能会拒绝该次请求

#UA伪装：将爬虫对应请求的身份载体伪装成浏览器
"""import requests
if __name__ == "__main__":
    #UA伪装，将对应的User-agent封装到一个字典中
    headers = {

     'User - Agent: Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 64.0.3282.140 Safari / 537.36Edge / 18.17763'

    }
    url = 'https://www.sogou.com/web?'
    #处理url携带的参数：封装到字典中
    kw = input('enter a word：')
    param = {
        'query': kw
    }
    #对指定的url发起的请求是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param，headers=headers)

    page_text = response.text
    fileName = kw + '.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
        print(fileName,'保存成功！！')"""
import requests
#if __name__ == "__main__":
wd=input('enter a word')
#1.
url="https://www.sogou.com/web?"
#2.将请求参数设定为动态的
param={
    "query":wd
}
#UA伪装
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
#3.params传参
response=requests.get(url=url,params=param,headers=headers)
#4.手动设置响应数据的编码,处理中文乱码问题
response.encoding='utf-8'
#5.text返回的是字符串形式的响应数据
page_text=response.text

filename=wd+'.html'

with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)