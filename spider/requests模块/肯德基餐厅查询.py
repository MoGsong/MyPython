import requests
#爬取肯德基餐厅位置信息(有关于ajax刷新页面的数据采集)
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#动态生成城市
city=input('enter a city name:')
data={
    'cname': '',
    'pid': '',
    'keyword': city,
    'pageIndex': '1',
    'pageSize': '10',
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = requests.post(url=url,data=data,headers=headers)

page_text=response.json()
print(page_text)

#这里文件操作可以覆盖写入,也可以追加写入

fp=open('/kfc.text','w',encoding='utf-8')


for dic in page_text['Table1']:
    addr=dic['addressDetail']
    print(addr)
    fp.write(addr+'\n')
fp.clouse()