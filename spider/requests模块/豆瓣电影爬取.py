import json
import requests
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action' : '',
        'start':'0',   #从库中第几部电影去取，可修改
        'limit':'5',   #一次取出的电影数，可修改
    }
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url=url,params=param,headers=headers)
    list_date = response.json()

    fp = open('douban.json', 'w', encoding='utf-8')
    json.dump(list_date,fp=fp,ensure_ascii=False)

    print('over')