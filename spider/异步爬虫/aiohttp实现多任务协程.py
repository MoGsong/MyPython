import asyncio
import time
import requests
import aiohttp
#ClientSession
urls =[
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]
start = time.time()
async def get_page(url):
    print('loading',url)
    #request请求是同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    #aiohttp:基于异步网络请求的模块
    #rep = requests.get(url=url)
    async with aiohttp.ClientSession() as session:
        #GET POST 是对应的请求方式
       async with await session.get(url) as reponse:     #await挂起
           #text()方法返回字符串形式
           #read()二进制
           #json()json对象
           page_text = await reponse.text()          #获取响应数据操作之前一定要使用awit进行挂起
           print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(end-start)