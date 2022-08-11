"""import requests
import json
import time
# import os
#
# def __init__(self, path='./'):
#     # save the path
#     self.path = path
#     if not os.name.exists(path):
#         os.mkdir(path)

def get_Disstid(url):
    headers={
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Referer":"https://y.qq.com/portal/playlist.html",
        "Host":"c.y.qq.com",
    }
# 1访问入口得到音乐列表的disstid
    res = requests.get(url,headers=headers).text
    re=res.strip("getPlaylist()")
    r=json.loads(re)
    for x in r["data"]["list"]:
        # 用得到的dissid进行拼接得到新的url
        sub_url = " https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid={0}&format=jsonp&g_tk=5381&jsonpCallback=playlistinfoCallback&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0".format(x["dissid"])
#2访问音乐分类，得到歌单的songmid，songname
        headers["referer"]="https://y.qq.com/n/yqq/playsquare/{0}.html".format(x["dissid"])
        res = requests.get(sub_url, headers=headers).text
        re = res.strip("playlistinfoCallback()")
        r = json.loads(re)
        for x in r["cdlist"][0]["songlist"]:
            songmid = x["songmid"]
            songname = "C400{0}.m4a".format(songmid)
            song = x["songname"]
            key_url = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback20480960151150063&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback20480960151150063&uin=0&songmid={0}&filename={1}&guid=9602668140".format(
                songmid, songname)
#3.访问播放页面，得到每首歌的vkey
            headers["Referer"] = "https://y.qq.com/portal/player.html"
            res = requests.get(key_url, headers=headers).text
            re = res.strip("MusicJsonCallback20480960151150063()")
            r = json.loads(re)
            for x in r["data"]["items"]:
                vkey = x["vkey"]
                song_url = "http://dl.stream.qqmusic.qq.com/{0}?vkey={1}&guid=9602668140&uin=0&fromtag=66".format(
                    songname, vkey)
#4.访问音乐文件下载
                headers["Host"]="dl.stream.qqmusic.qq.com"
                del headers["Referer"]
                res=requests.get(song_url,headers=headers,stream=True)
                filename = r"music/{0}.m4a".format(song)
                # basedir = os.path.dirname(__file__)
                # print("basedir:" + basedir)
                # upload_path = os.path.join(basedir, "static/upload", filename)
                # if not os.path.exists(upload_path):
                #     os.mkdir(upload_path)
                print(song)
                with open(filename,"wb") as f:
                    f.write(res.raw.read())
if __name__ == '__main__':
    sin = 0
    ein = 29
    sum = 5620
    while True:
        url="https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.7709971027608087&g_tk=5381&jsonpCallback=getPlaylist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin={0}&ein={1}".format(sin,ein)
        sub_url_list=get_Disstid(url)
        if ein<5620:
            sub_url_list = get_Disstid(url)
            sin+=30
            ein+=30
        else:
            break
        time.sleep(1)
"""
# import requests
# import re
# import os
# import json
# import time as t


'''class QQmusic():
    """下载qq音乐"""

    def __init__(self):
        """初始化"""
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.baidu.com/',
            'Connection': 'keep-alive',
        }
        self.names = []
        self.order = ' '

    def search(self):
        """搜索"""
        w = input("请输入歌曲名： ")
        url_0 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61460539676714578&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w={0}&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0".format(
            w)
        res_0 = requests.get(url_0, headers=self.headers)  # 第一层，搜索页
        res_0.encoding = res_0.apparent_encoding
        res_0 = res_0.json()  # dict
        music_list = res_0["data"]["song"]["list"]
        print("共计" + str(len(music_list)) + "结果： ")

        all_singers = []
        a = 0
        for music in music_list:
            singer = music["singer"][0]["title"]  # 歌手名
            name = str(a) + "  " + music["title"]  # 歌曲名
            all_singers.append(singer)
            self.names.append(name)
            a = a + 1
        infs = dict(zip(self.names, all_singers))
        infs = json.dumps(infs, ensure_ascii=False, indent=4, separators=(',', ':'))
        infs = infs.replace('"', ' ')
        infs = infs.replace(':', '——————')
        print(infs)

        self.order = input("请输入歌曲前的序号：")
        songmid = res_0['data']['song']['list'][int(self.order)]['mid']
        url_1 = "https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D".format(
            songmid)
        res_1 = requests.get(url_1, headers=self.headers)
        res_1.encoding = res_1.apparent_encoding
        res_1 = res_1.json()  # dict
        purl = res_1['req_0']['data']['midurlinfo'][0]['purl']
        url_2 = "https://isure.stream.qqmusic.qq.com/" + purl
        return url_2

    def download(self):
        """下载"""
        res_2 = requests.get(self.search(), headers=self.headers).content
        fir = self.names[int(self.order)]
        tit = re.sub(r'\d+', '', fir)
        now = os.getcwd()
        now = os.path.join(now, "qq音乐 ")
        if not os.path.exists(now):
            os.mkdir(now)
        os.chdir(now)
        file_name = tit + '.m4a'
        with open(file_name, 'wb') as f:
            f.write(res_2)


one_file = QQmusic()
one_file.download()'''

import requests
import re
import os
import json
import time as t


class QQmusic():
    """代码仅供学习"""

    def __init__(self):
        """初始化"""
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.baidu.com/',
            'Connection': 'keep-alive',
        }
        self.names = []
        self.order = ' '

    def search(self):
        """搜索"""
        w = input("请输入歌曲名： ")
        url_0 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61460539676714578&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w={0}&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0".format(
            w)
        res_0 = requests.get(url_0, headers=self.headers)  # 第一层，搜索页
        res_0.encoding = res_0.apparent_encoding
        res_0 = res_0.json()  # dict
        music_list = res_0["data"]["song"]["list"]
        print("共计" + str(len(music_list)) + "结果： ")

        all_singers = []
        a = 0
        for music in music_list:
            singer = music["singer"][0]["title"]  # 歌手名
            name = str(a) + "  " + music["title"]  # 歌曲名
            all_singers.append(singer)
            self.names.append(name)
            a = a + 1
        infs = dict(zip(self.names, all_singers))
        infs = json.dumps(infs, ensure_ascii=False, indent=4, separators=(',', ':'))
        infs = infs.replace('"', ' ')
        infs = infs.replace(':', '——————')
        print(infs)

        self.order = input("请输入歌曲前的序号：")
        songmid = res_0['data']['song']['list'][int(self.order)]['mid']
        url_1 = "https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D".format(songmid)

        res_1 = requests.get(url_1, headers=self.headers)
        res_1.encoding = res_1.apparent_encoding
        res_1 = res_1.json()  # dict
        purl = res_1['req_0']['data']['midurlinfo'][0]['purl']
        url_2 = "https://isure.stream.qqmusic.qq.com/" + purl
        return url_2

    def download(self):
        """下载"""
        res_2 = requests.get(self.search(), headers=self.headers).content
        fir = self.names[int(self.order)]
        tit = re.sub(r'\d+', '', fir)
        now = os.getcwd()
        now = os.path.join(now, "qq音乐 ")
        if not os.path.exists(now):
            os.mkdir(now)
        os.chdir(now)
        file_name = tit + '.m4a'
        with open(file_name, 'wb') as f:
            f.write(res_2)


one_file = QQmusic()
one_file.download()


'''import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'Referer': 'http://music.163.com/',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

# 歌单的url地址
play_url = 'http://music.163.com/playlist?id=5041773022'

# 获取页面内容
s = requests.session()
response = s.get(play_url, headers=headers).content

# 使用bs4匹配出对应的歌曲名称和地址
s = BeautifulSoup(response, 'lxml')
main = s.find('ul', {'class': 'f-hide'})

lists = []
for music in main.find_all('a'):
    list = []
    # print('{} : {}'.format(music.text, music['href']))
    musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
    musicName = music.text
    # 单首歌曲的名字和地址放在list列表中
    list.append(musicName)
    list.append(musicUrl)
    # 全部歌曲信息放在lists列表中
    lists.append(list)

print(lists)

# 下载列表中的全部歌曲，并以歌曲名命名下载后的文件，文件位置为当前文件夹
for i in lists:
    url = i[1]
    name = i[0]
    try:
        print('正在下载', name)
        urllib.request.urlretrieve(url, './music/%s.mp3' % name)
        print('下载成功')
    except:
        print('下载失败')'''


# import urllib.request
# import json
# import re
# import urllib.parse
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# name = input("输入你想听的歌名or歌名+歌手:")
# name = urllib.parse.quote(name)
# url = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w="+name
#
# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
# }
#
# def network(url):
#     request_url = urllib.request.Request(url,headers=headers)
#     response = urllib.request.urlopen(request_url).read().decode('utf-8')
#     return response
#
# def download(songmid,music_name):
# #json数据
#     json_url = "https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback8796342823761736&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback8796342823761736&uin=0&" \
#            "songmid="+songmid+"&filename=C400"+songmid+".m4a&guid=4626869183"
#     html = network(json_url)
# #找到json中music的信息
#     music_json = json.loads(re.findall(r'^\w+\((.*)\)$',html)[0])
#     filename = music_json['data']['items'][0]['filename']
#     vkey = music_json['data']['items'][0]['vkey']
# #歌曲的下载链接
#     download_url = "http://dl.stream.qqmusic.qq.com/"+filename+"?vkey="+vkey+"&guid=4626869183&uin=0&fromtag=66"
#     ret_url = urllib.request.Request(download_url,headers=headers)
#     music_url = urllib.request.urlopen(ret_url).read()
#     with open("./"+music_name+".m4a", "wb") as fb:
#         fb.write(music_url)
#
# def get():
# #加载Chromedriver,百度chromedriver.exe，下载与自己chrome版本一致的。
#     option = webdriver.ChromeOptions()
#     option.add_argument('headless')
#     driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=option)
# #请自行修改加载的路径
#     driver.get(url)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "js_song")))
#     music = driver.find_element_by_class_name('js_song')
#     href = music.get_attribute('href')
#     music_name = music.get_attribute('title')
# #匹配到歌曲的id
#     songmid = re.findall(r'https://y.qq.com/n/yqq/song/(\S+).html',href)[0]
#     download(songmid,music_name)
# if __name__ == '__main__':
#     get()