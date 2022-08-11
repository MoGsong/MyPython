import asyncio
import time
async def request(url):
    print("loading......",url)
    #在异步协程中如果出现同步模块相关代码就无法实现异步
    #time.sleep(2)
    #遇到阻塞，必须进行手动挂起 await
    await asyncio.sleep(2)
    print("over!")
start = time.time()
urls = [
    'www.baidu.com',
    'www.sougou.com',
    'www.houbanjia.com'

]
#任务列表：任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()
#将任务列表封装到wait
loop.run_until_complete(asyncio.wait(stasks))

print(time.time()-start)