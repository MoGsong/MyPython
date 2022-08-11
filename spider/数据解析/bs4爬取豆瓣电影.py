import requests
from bs4 import BeautifulSoup
#序号/电影名/评分/推荐语/链接

url_list = []
num_temp = 0
while num_temp < 250:
    url = 'https://movie.douban.com/top250?start='+ str(num_temp) +'&filter='
    url_list.append(url)
    num_temp = num_temp + 25
for url_temp in url_list:
    res = requests.get(url_temp)
    bs = BeautifulSoup(res.text,'html.parser')
    movie_list = bs.find_all('ol',class_="grid_view")
    for i in movie_list[0].find_all('li'):
        try:
            num = i.find('em',class_='''''').text
            name = i.find('span',class_='title').text
            grades = i.find('span',class_='rating_num').text
            review = i.find('p',class_='quote').text
            link = i.find('a')['href']
        except(AttributeError):#因为有的电影没有推荐语，会报错
            review = ' \n\n'
        print('序号：'+ num + '\n 电影名：' + name + ' 评分：' + grades + ' 推荐语：' + review + ' 电影连接：' + link)
