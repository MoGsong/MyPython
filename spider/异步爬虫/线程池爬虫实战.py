#import  json
import re
import requests
from lxml import etree
from multiprocessing.dummy import  Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning                    #忽略证书警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    "Connection": 'keep-alive'
}
'''param = {
    'contId': 'xx',                              #id封装到字典进行传参
    #'mrd': '0.01707224563991394',                    #是一个随机值，不用当参数
    #'shareType': '1'
}
#ajax 请求url
jump_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1728425&mrd=0.8752336322864998'
json_list = requests.get(url=jump_url,headers=headers,json=param).json()
for dict in json_ids['list']:  # 提取list中的字典，ID在页面的list中，遍历ID
            id_list.append(dict['ID'])
            print('ID')
'''

#线程池只处理阻塞耗时的操作
#对下述url发起请求获取详情页的url和视频的名称
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')                #标签属性定位

video_url= ['https://video.pearvideo.com/mp4/third/20210430/cont-1728371-10008579-141022-hd.mp4',   #第一个视频
    'https://video.pearvideo.com/mp4/third/20210430/cont-1728373-10008579-141600-hd.mp4' ,               #第二个视频
    'https://video.pearvideo.com/mp4/adshort/20210430/cont-1728439-15668335_adpkg-ad_hd.mp4' ,           #3 有一个可变id在
    'https://video.pearvideo.com/mp4/short/20210430/cont-1728425-15668170-hd.mp4']   #4 srcUrl位于request headers的General中
urls = []       #视频的名字和链接
name = []
for li in li_list:
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]   #完整的详情页url
    n = li.xpath('./div/a/div[2]/text()')[0] +'.mp4'                  #层级选择文本
    name.append(n)
    #name = li.xpath('.//div[@class="vervideo-title"]')[0].text+'.mp4'    #属性定位文本
    #print(detail_url,name)
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    #print(detail_page_text)
    #print('1',detail_page_text.headers)                             #响应头
    #print('2',requests.Request(headers))                             #请求头headers
    #print('3',detail_page_text.url)                                 #响应url
    #detail_mp4_url = 'https://www.pearvideo.com/'   +  detail_page_text.title('General.url')
    #这是一个动态的链接，但是MP4是非动态，可以用正则来进行数据解析

    #ex = 'srcUrl="(.*?)",vdoUrl'    #srcUrl:"https://[^\s]+(?=\S)\-[^\s]+\.[A-Za-z0-9]+" srcUrl:."https://(.*?)[^\s]+(?=\S)    #匹配不到.mp4文件
    #ex = 'https://[^\s]+(?=\S)\-[^\s]+\.[A-Za-z0-9]+'
    #video_url = re.findall(ex,detail_page_text,re.S)
    dic = {
        'name':name,
        'url':video_url,
    }
    #urls.append(dic)
    urls = dic
print('/////////////////////////////////////////////////////////')
print(urls)
print(video_url)
print(name)
print('/////////////////////////////////////////////////////////')

urlss = []
for i in range(0,len(name)):
    n = name[i]
    u = video_url[i]
    dic2={
        'name': n,
        'url': u,
    }
    urlss.append(dic2)

print('/////////////////////////////////////////////////////////')
print(urlss)

#使用线程池对视频数据进行请求
def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载！')
    data = requests.get(url=url,headers=headers,verify=False,stream=True,allow_redirects=False).content
    #chijuhuacunchu
    with open(dic['name'],'wb') as fp:
        fp.write(data)
        print(dic['name'],'下载成功！')
#try:
pool = Pool(4)
pool.map(get_video_data,urlss)
#except Exception as exp:
    #print(exp)
pool.close()
pool.join()