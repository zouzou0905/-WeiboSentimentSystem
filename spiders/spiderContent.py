'''import time
import requests
import csv
import os
import numpy as np
from datetime import datetime
# 爬取热门时间线上的文章数据
def init():
    if not os.path.exists('./articleData.csv'):
        with open('./articleData.csv','w',encoding='utf-8',newline='')as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([
                'id',
                'likeNum',
                'commentsLen',
                'reposts_count',
                'region',
                'content',
                'contentLen',
                'created_at',
                'type',
                'detailUrl',
                'authorAvatar',
                'authorName',
                'authorDetail',
                'isVip'
            ])

def writerRow(row):
    with open('./articleData.csv','a',encoding='utf-8',newline='')as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow(row)

def get_data(url,params):
    headers = {
        'Cookie': 'SINAGLOBAL=4307542057500.3223.1717571699283; UOR=,,cn.bing.com; SCF=ApozugwcuzQLTGgRgQ6GbqqcZTMXtPWmcjnhBekgh2sSIrtOw0eDPyfjr3ZfWF87k5P_h1BQAU4b96esZdqBQGY.; SUB=_2A25LZvoRDeRhGeFH6VYU8yjEwj6IHXVoGnPZrDV8PUNbmtB-LU_4kW9Ne4t1NZuXdufD8Q-9G6YyRmpttc_2GBGh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0OniMibjDQzvLY8zRHhpZ5JpX5o275NHD95QN1KzXSKec1h.EWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.ESh-0Son4entt; ALF=1718338790; ULV=1717740902982:4:4:4:3470754407274.255.1717740902964:1717731772022; XSRF-TOKEN=84icyK57B-GZziasnMHCF6b8; WBPSESS=XzliALnG2z6nsoGsiVOFCw7XVYw3h7QA4Fp3GZMxbVCWBbeQ9oPctzf5RN6yVIlxIA2fTnz8fwdVWj2vTzLstfelsOj-VZlb6ioTTUNDmOMias-tLmQxzP6cB_QOaqwIWcE-NMGZxi-Lf2b0eS0Acg==; PC_TOKEN=bcacd0158d',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response=requests.get(url,headers=headers,params=params)
    #print(response.json())
    if response.status_code==200:
        return response.json()['statuses']
    else:
        return None

def getAllTypelist():
    typelist=[]
    with open('./navData.csv','r',encoding='utf-8')as reader:
        readerCsv=csv.reader(reader)
        for nav in readerCsv:
            typelist.append(nav)
    return typelist

def parse_json(response,type):
    for article in response:
        id = article['id']
        likeNum = article['attitudes_count']
        commentsLen=article['comments_count']
        reposts_count=article['reposts_count']
        try:
            region = article['region_name'].replace('发布于','')
        except:
            region='无'
        content=article['text_raw']
        contentLen=article['textLength']
        created_at=datetime.strptime(article['created_at'],'%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d')
        type = type
        try:
            detailUrl = 'https://weibo.com/'+ str(article['id']) + '/' +str(article['mblogid'])
        except:
            detailUrl='无'
        authorAvatar =article['user']["avatar_large"]
        authorName = article['user']['screen_name']
        authorDetail = 'https://weibo.com/u/'+str(article['user']['id'])
        isVip= article['user']['v_plus']
        writerRow([
            id,
            likeNum,
            commentsLen,
            reposts_count,
            region,
            content,
            contentLen,
            created_at,
            type,
            detailUrl,
            authorAvatar,
            authorName,
            authorDetail,
            isVip
        ])


def start(typeNum=3,pageNume=2):
    articleurl='https://www.weibo.com/ajax/feed/hottimeline'
    init()
    typelist=getAllTypelist()
    typeNumCount=0

    # params = {
    #     'group_id': type[1],
    #     'containerid': type[2],
    #     'max_id': page,
    #     'count': 10,
    #     'extparam': 'discover|new_feed'
    # }
    # response = get_data(articleurl, params)

    for type in typelist:
        if typeNumCount > typeNum:return
        time.sleep(2)
        for page in range(0,pageNume):
            print('正在爬取的 %s 类型中的第%s页文章数据'%(type[0],page+1))
            time.sleep(1)
            params={
                'group_id':type[1],
                'containerid':type[2],
                'max_id':page,
                'count':10,
                'extparam':'discover|new_feed'
            }
            response = get_data(articleurl,params)
            parse_json(response,type[0])
        typeNumCount += 1


if __name__ == '__main__':
    start()'''

import time
import requests
import  csv
import  os
import numpy as np
from datetime import datetime
# 爬取热门时间线上的文章数据
def init():
    if not os.path.exists('./articleData.csv'):
        with open('./articleData.csv','w',encoding='utf-8',newline='')as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow([
                'id',
                'likeNum',
                'commentsLen',
                'reposts_count',
                'region',
                'content',
                'contentLen',
                'created_at',
                'type',
                'detailUrl',
                'authorAvatar',
                'authorName',
                'authorDetail',
                'isVip'
            ])

def writerRow(row):
    with open('./articleData.csv','a',encoding='utf-8',newline='')as csvFile:
            writer=csv.writer(csvFile)
            writer.writerow(row)

def get_data(url,params):
    headers = {
        'Cookie': 'SINAGLOBAL=4307542057500.3223.1717571699283; UOR=,,cn.bing.com; SCF=ApozugwcuzQLTGgRgQ6GbqqcZTMXtPWmcjnhBekgh2sSIrtOw0eDPyfjr3ZfWF87k5P_h1BQAU4b96esZdqBQGY.; SUB=_2A25LZvoRDeRhGeFH6VYU8yjEwj6IHXVoGnPZrDV8PUNbmtB-LU_4kW9Ne4t1NZuXdufD8Q-9G6YyRmpttc_2GBGh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0OniMibjDQzvLY8zRHhpZ5JpX5o275NHD95QN1KzXSKec1h.EWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.ESh-0Son4entt; ALF=1718338790; ULV=1717740902982:4:4:4:3470754407274.255.1717740902964:1717731772022; XSRF-TOKEN=84icyK57B-GZziasnMHCF6b8; WBPSESS=XzliALnG2z6nsoGsiVOFCw7XVYw3h7QA4Fp3GZMxbVCWBbeQ9oPctzf5RN6yVIlxIA2fTnz8fwdVWj2vTzLstfelsOj-VZlb6ioTTUNDmOMias-tLmQxzP6cB_QOaqwIWcE-NMGZxi-Lf2b0eS0Acg==; PC_TOKEN=bcacd0158d',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response=requests.get(url,headers=headers,params=params)
    #print(response.json())
    if response.status_code==200:
        return response.json()['statuses']
    else:
        return None

def getAllTypelist():
    typelist=[]
    with open('./navData.csv','r',encoding='utf-8')as reader:
        readerCsv=csv.reader(reader)
        next(readerCsv)
        for nav in readerCsv:
            typelist.append(nav)
    return typelist

def parse_json(response,type):
    for article in response:
        id = article['id']
        likeNum = article['attitudes_count']
        commentsLen=article['comments_count']
        reposts_count=article['reposts_count']
        try:
            region = article['region_name'].replace('发布于','')
        except:
            region='无'
        content=article['text_raw']
        contentLen=article['textLength']
        created_at=datetime.strptime(article['created_at'],'%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d')
        type = type
        try:
            detailUrl = 'https://weibo.com/'+ str(article['id']) + '/' +str(article['mblogid'])
        except:
            detailUrl='无'
        authorAvatar =article['user']["avatar_large"]
        authorName = article['user']['screen_name']
        authorDetail = 'https://weibo.com/u/'+str(article['user']['id'])
        isVip= article['user']['v_plus']
        writerRow([
            id,
            likeNum,
            commentsLen,
            reposts_count,
            region,
            content,
            contentLen,
            created_at,
            type,
            detailUrl,
            authorAvatar,
            authorName,
            authorDetail,
            isVip
        ])


def start(typeNum=3,pageNume=2):
    articleurl='https://www.weibo.com/ajax/feed/hottimeline'
    init()
    typelist=getAllTypelist()
    typeNumCount=0

    # params = {
    #     'group_id': type[1],
    #     'containerid': type[2],
    #     'max_id': page,
    #     'count': 10,
    #     'extparam': 'discover|new_feed'
    # }
    # response = get_data(articleurl, params)

    for type in typelist:

        if typeNumCount> typeNum :return
        time.sleep(2)
        for page in range(0,pageNume):
            print('正在爬取的 %s 类型中的第%s页文章数据'%(type[0],page+1))
            time.sleep(1)
            params={
                'group_id':type[1],
                'containerid':type[2],
                'max_id':page,
                'count':10,
                'extparam':'discover|new_feed'
            }
            response=get_data(articleurl,params)
            parse_json(response,type[0])
        typeNumCount+=1


if __name__=='__main__':
    start()