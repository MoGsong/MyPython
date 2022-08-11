import requests
url = 'http://192.168.125.13'   # 'http://172.16.1.129'
r = requests.get(url)
print(r.content)
print(r.headers['Server'])