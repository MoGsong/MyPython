import asyncio
import time
import requests
urls =[
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]
start = time.time()
async def get_page(url):
    print('loading',url)
    #request请求是同步的，必须使用基于异步的网络请求模块进行指定url的请求发送
    #aiohttp:基于异步网络请求的模块
    rep = requests.get(url=url)
    print('loading',rep.text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(end-start)