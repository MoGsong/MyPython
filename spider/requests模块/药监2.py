import requests
import json #调用screenflow
if __name__ == "__main__":
    url = 'https://125.35.6.84:81/xk/itownert/portalAction.do?method=getXkzsList'   #url是同一个(药监网址变更了)
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    id_list = []
    for page in range(1,6):
        page = str(page)
        date={                                          #进行分页操作
            'on' : 'ture',
            'page' : page,
            'pageSiz ': '15',                           #动态获取参数为ID
            'productName ': '',
            'conditionType' : '1',
            'applyname' : '',
            'applysn' : '',

        }
        json_ids = requests.post(url=url ,date=date,headers=headers).json()   #返回Json数据

        for dict in json_ids['list']:  # 提取list中的字典，ID在页面的list中，遍历ID
            id_list.append(dict['ID'])
            print('ID')

    all_date_list = []
    #存储ID，且是字典类型数据

    #获取企业详情数据
    post_url = 'https://125.35.6.84:81/xk/itownert/portalAction.do?method=getXkzsList'
    for id in id_list:
        date = {
        'id' :  id
        }
        detail_json = requests.post(url=post_url,headers=headers,date=date).json()
        print(detail_json)
        all_date_list.append(detail_json)
    #持久化数据
    fp = open('.allDate.json','w',encoding ='utf-8')
    json.dump(all_date_list,fp=fp,ensure_ascii=False)
    print('over')