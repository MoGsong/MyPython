"""import time
#模拟单线程串行方式
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print("下载成功：", str)

name_list = ['xiaozi','aa','bb','cc']
start_time = time.time()

for i in range(len(name_list)):
    get_page(name_list[i])

end_time = time.time()
print('%d second'%(end_time-start_time))"""

import time
from multiprocessing.dummy import Pool
start_time = time.time()
#模拟线程池
def get_page(str):
    print("正在下载：\n",str)
    time.sleep(2)
    print("下载成功：", str)

name_list = ['xiaozi','aa','bb','cc']

#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表传给GET—page进行处理
pool.map(get_page,name_list)
end_time = time.time()
print(end_time-start_time)

