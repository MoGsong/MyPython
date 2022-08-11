import requests
# open IIC DAV
url = 'heep://172.16.1.129'
r = requests.options(url)
# print(r.headers)
# print(r.headers['Allow'])
# print(r.headers['Public'])
result = r.headers['Public']
if result.find("PUT") and result.find("MOVE"):
    print("exist iis put val")
    print(result)
else:
    print("not exist")