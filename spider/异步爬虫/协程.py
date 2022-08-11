import asyncio
async def  request(url):
    print("正在请求的url是",url)
    print("请求成功", url)
    return url

c = request('www.baidu.com')        #返回一个协程对象

#创建一个事件循环对象
#loop = asyncio.get_event_loop()

#将协程对象注册到loop中,然会启动loop
#loop.run_until_complete(c)
#asyncio.run(c)

#task
#loop = asyncio.get_event_loop()
#task = loop.create_task(c)         #基于循环对象的
#print(task)

#loop.run_until_complete(task)
#print(task)

#future
#loop = asyncio.get_event_loop()
#futrue = asyncio.ensure_future(c)
#print(futrue)

#loop.run_until_complete(futrue)
#print(futrue)

def callback_func(task):
    #result任务对象对应函数的返回值
    print(task.result())
#绑定回调
loop= asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象
task.add_done_callback(callback_func)
loop.run_until_complete(task)