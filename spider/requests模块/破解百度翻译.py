import json
import requests                   #POST请求
if __name__ == "__main__":
    #指定url
    post_url = ' https://fanyi.baidu.com/sug'
    #UA伪装
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    #post请求参数处理
    word = input('enter a word')
    date = {
        'kw' : word
    }
    #请求发送
    response = requests.post(url=post_url,data=date,headers=headers)
    #获取响应数据,json返回是一个对象obj（如果确认我们响应数据是json才可以用）
    dic_obj =  response.json()
    print(dic_obj)
    #持久化存储
    fileName = word +'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over')
