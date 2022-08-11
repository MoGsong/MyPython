import requests
from lxml import etree
url ='https://www.cnblogs.com/xyz-6996/p/14071851.html'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
print(page_text)
graphs = tree.xpath('//*[@id="blog-news"]')
print(graphs)
with open('./cute.txt', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
