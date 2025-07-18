'''import requests
import csv
import os
from datetime import datetime
# 爬取文章的评论数据
def init():
    if not os.path.exists('commentsData.csv'):
        with open('commentsData.csv','w',encoding='utf8',newline='') as csvfile:
            wirter = csv.writer(csvfile)
            wirter.writerow([
                'articleId',
                'created_at',
                'like_counts',
                'region',
                'content',
                'authorName',
                'authorGender',
                'authorAddress',
                'authorAvatar'
            ])

def wirterRow(row):
        with open('commentsData.csv','a',encoding='utf8',newline='') as csvfile:
            wirter = csv.writer(csvfile)
            wirter.writerow(row)

def get_html(url,id):
    headers = {
        'Cookie': 'SINAGLOBAL=4307542057500.3223.1717571699283; UOR=,,cn.bing.com; SCF=ApozugwcuzQLTGgRgQ6GbqqcZTMXtPWmcjnhBekgh2sSIrtOw0eDPyfjr3ZfWF87k5P_h1BQAU4b96esZdqBQGY.; SUB=_2A25LZvoRDeRhGeFH6VYU8yjEwj6IHXVoGnPZrDV8PUNbmtB-LU_4kW9Ne4t1NZuXdufD8Q-9G6YyRmpttc_2GBGh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0OniMibjDQzvLY8zRHhpZ5JpX5o275NHD95QN1KzXSKec1h.EWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.ESh-0Son4entt; ALF=1718338790; ULV=1717740902982:4:4:4:3470754407274.255.1717740902964:1717731772022; XSRF-TOKEN=84icyK57B-GZziasnMHCF6b8; WBPSESS=XzliALnG2z6nsoGsiVOFCw7XVYw3h7QA4Fp3GZMxbVCWBbeQ9oPctzf5RN6yVIlxIA2fTnz8fwdVWj2vTzLstfelsOj-VZlb6ioTTUNDmOMias-tLmQxzP6cB_QOaqwIWcE-NMGZxi-Lf2b0eS0Acg==; PC_TOKEN=bcacd0158d',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    params = {
        'is_show_bulletin':2,
        'id':id
    }
    response = requests.get(url,headers=headers,params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_json(response,articleId):
    commentList = response['data']
    for comment in commentList:
        created_at = datetime.strptime(comment['created_at'],"%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d")
        like_counts = comment['like_counts']
        authorName = comment['user']['screen_name']
        authorGender = comment['user']['gender']
        authorAddress = comment['user']['location'].split(' ')[0]
        authorAvatar = comment['user']['avatar_large']
        try:
            region = comment['source'].replace('来自','')
        except:
            region = '无'
        content = comment['text_raw']
        wirterRow([
            articleId,
            created_at,
            like_counts,
            region,
            content,
            authorName,
            authorGender,
            authorAddress,
            authorAvatar,
        ])

def start():
    init()
    url = 'https://www.weibo.com/ajax/statuses/buildComments'
    with open('./articleData.csv','r',encoding='utf8') as readerFile:

        reader = csv.reader(readerFile)
        for article in reader:

            articleId = article[0]
            response = get_html(url,articleId)
            #print(response)
            parse_json(response,articleId)
            break

if __name__ == '__main__':
    start()'''

import requests
import csv
import os
from datetime import datetime
# 爬取文章的评论数据
def init():
    if not os.path.exists('articleComments.csv'):
        with open('articleComments.csv','w',encoding='utf8',newline='') as csvfile:
            wirter = csv.writer(csvfile)
            wirter.writerow([
                'articleId',
                'created_at',
                'like_counts',
                'region',
                'content',
                'authorName',
                'authorGender',
                'authorAddress',
                'authorAvatar'
            ])

def wirterRow(row):
        with open('articleComments.csv','a',encoding='utf8',newline='') as csvfile:
            wirter = csv.writer(csvfile)
            wirter.writerow(row)

def get_html(url,id):
    headers = {
        'Cookie': 'SINAGLOBAL=4307542057500.3223.1717571699283; UOR=,,cn.bing.com; SCF=ApozugwcuzQLTGgRgQ6GbqqcZTMXtPWmcjnhBekgh2sSIrtOw0eDPyfjr3ZfWF87k5P_h1BQAU4b96esZdqBQGY.; SUB=_2A25LZvoRDeRhGeFH6VYU8yjEwj6IHXVoGnPZrDV8PUNbmtB-LU_4kW9Ne4t1NZuXdufD8Q-9G6YyRmpttc_2GBGh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0OniMibjDQzvLY8zRHhpZ5JpX5o275NHD95QN1KzXSKec1h.EWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.ESh-0Son4entt; ALF=1718338790; ULV=1717740902982:4:4:4:3470754407274.255.1717740902964:1717731772022; XSRF-TOKEN=84icyK57B-GZziasnMHCF6b8; WBPSESS=XzliALnG2z6nsoGsiVOFCw7XVYw3h7QA4Fp3GZMxbVCWBbeQ9oPctzf5RN6yVIlxIA2fTnz8fwdVWj2vTzLstfelsOj-VZlb6ioTTUNDmOMias-tLmQxzP6cB_QOaqwIWcE-NMGZxi-Lf2b0eS0Acg==; PC_TOKEN=bcacd0158d',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    params = {
        'is_show_bulletin':2,
        'id':id
    }
    response = requests.get(url,headers=headers,params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_json(response,articleId):
    commentList = response['data']
    for comment in commentList:
        created_at = datetime.strptime(comment['created_at'],"%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d")
        like_counts = comment['like_counts']
        authorName = comment['user']['screen_name']
        authorGender = comment['user']['gender']
        authorAddress = comment['user']['location'].split(' ')[0]
        authorAvatar = comment['user']['avatar_large']
        try:
            region = comment['source'].replace('来自','')
        except:
            region = '无'
        content = comment['text_raw']
        wirterRow([
            articleId,
            created_at,
            like_counts,
            region,
            content,
            authorName,
            authorGender,
            authorAddress,
            authorAvatar,
        ])

def start():
    init()
    url = 'https://www.weibo.com/ajax/statuses/buildComments'
    with open('./articleData.csv','r',encoding='utf8') as readerFile:
        reader = csv.reader(readerFile)
        next(reader)
        for article in reader:
            print('正在爬取的 %s 评论数据' % (article[0]))
            articleId = article[0]
            response = get_html(url,articleId)
            #print(response)
            parse_json(response,articleId)


if __name__ == '__main__':
    start()