import requests

url = 'https://www.baidu.com/s?wd=ip'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers,proxies={"https:":'https://222.110.147.50:3128'}).text                #117.140.154.86（本机)

with open('ip.html','w',encoding='utf-8')as fp:
    fp.write(page_text)



"""# -*- coding: UTF-8 -*-

'''
Python 3.x
无忧代理IP Created on 2018年05月11日
描述：本DEMO演示了使用爬虫（动态）代理IP请求网页的过程，代码使用了多线程
逻辑：每隔5秒从API接口获取IP，对于每一个IP开启一个线程去抓取网页源码
@author: www.data5u.com
'''
import requests;
import time;
import threading;
import urllib3;

ips = [];

# 爬数据的线程类
class CrawlThread(threading.Thread):
    def __init__(self,proxyip):
        super(CrawlThread, self).__init__();
        self.proxyip=proxyip;
    def run(self):
        # 开始计时
        start = time.time();
        #消除关闭证书验证的警告
        urllib3.disable_warnings();
        #使用代理IP请求网址，注意第三个参数verify=False意思是跳过SSL验证（可以防止报SSL错误）
        html=requests.get(url=targetUrl, proxies={"http" : 'http://' + self.proxyip, "https" : 'https://' + self.proxyip}, verify=False, timeout=15).content.decode()
        # 结束计时
        end = time.time();
        # 输出内容
        print(threading.current_thread().getName() +  "使用代理IP, 耗时 " + str(end - start) + "毫秒 " + self.proxyip + " 获取到如下HTML内容：\n" + html + "\n*************")

# 获取代理IP的线程类
class GetIpThread(threading.Thread):
    def __init__(self,fetchSecond):
        super(GetIpThread, self).__init__();
        self.fetchSecond=fetchSecond;
    def run(self):
        global ips;
        while True:
            # 获取IP列表
            res = requests.get(apiUrl).content.decode()
            # 按照\n分割获取到的IP
            ips = res.split('\n');
            # 利用每一个IP
            for proxyip in ips:
                if proxyip.strip():
                    # 开启一个线程
                    CrawlThread(proxyip).start();
            # 休眠
            time.sleep(self.fetchSecond);

if __name__ == '__main__':
    # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
    order = "    " ,r"请把这里替换为您的IP提取码";
    # 获取IP的API接口
    apiUrl = "http://dynamic.goubanjia.com/dynamic/get/" + order + ".html";
    # 要抓取的目标网站地址
    targetUrl = "http://pv.sohu.com/cityjson?ie=utf-8";
    # 获取IP时间间隔，建议为5秒
    fetchSecond = 5;
    # 开始自动获取IP
    GetIpThread(fetchSecond).start();"""