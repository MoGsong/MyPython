from lxml import etree
import requests
import re
response = requests.get('http://www.lagou.com/jobs/2101463.html')
resHtml = response.text
html = etree.HTML(resHtml)
try:
    title = html.xpath('//h2[@title]')[0].attrib['title']
#salary= html.xpath('//span[@class="red"]')[0].text
    salary = html.xpath('//dd[@class="job_request"]/p/span')[0].text
    worklocation = html.xpath('//dd[@class="job_request"]/p/span')[1].text
    experience = html.xpath('//dd[@class="job_request"]/p/span')[2].text
    education = html.xpath('//dd[@class="job_request"]/p/span')[3].text
    worktype = html.xpath('//dd[@class="job_request"]/p/span')[4].text
    Temptation = html.xpath('//dd[@class="job_request"]/p[2]')[0].text
    print(salary,worklocation,experience,education,worktype,Temptation)
    description_tag = html.xpath('//dd[@class="job_bt"]')[0]
    description =  etree.tostring( description_tag,encoding='utf-8')
#print description
    deal_descp =  re.sub('<.*?>','',description)
    print(deal_descp.strip())
    publisher_name =  html.xpath('//*[@class="publisher_name"]//@title')[0]
    pos =  html.xpath('//*[@class="pos"]')[0].text
    chuli_lv =  html.xpath('//*[@class="data"]')[0].text
    chuli_yongshi =  html.xpath('//*[@class="data"]')[1].text
    print(chuli_lv,chuli_yongshi,pos,publisher_name)
except:
    pass
