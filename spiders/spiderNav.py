'''import requests
import csv
import numpy as np
import os

def init():
    if not os.path.exists('./navData.csv'):
        with open('./navData.csv', 'w', encoding='utf-8',newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([
                'typeName',
                'gid',
                'containerid'
            ])

def writerRow(row):
    with open('./navData.csv', 'a', encoding='utf-8', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

def get_data(url):
    headers = {
        'Cookie':'SINAGLOBAL=4307542057500.3223.1717571699283; UOR=,,cn.bing.com; SCF=ApozugwcuzQLTGgRgQ6GbqqcZTMXtPWmcjnhBekgh2sSIrtOw0eDPyfjr3ZfWF87k5P_h1BQAU4b96esZdqBQGY.; SUB=_2A25LZvoRDeRhGeFH6VYU8yjEwj6IHXVoGnPZrDV8PUNbmtB-LU_4kW9Ne4t1NZuXdufD8Q-9G6YyRmpttc_2GBGh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0OniMibjDQzvLY8zRHhpZ5JpX5o275NHD95QN1KzXSKec1h.EWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.ESh-0Son4entt; ALF=1718338790; ULV=1717740902982:4:4:4:3470754407274.255.1717740902964:1717731772022; XSRF-TOKEN=84icyK57B-GZziasnMHCF6b8; WBPSESS=XzliALnG2z6nsoGsiVOFCw7XVYw3h7QA4Fp3GZMxbVCWBbeQ9oPctzf5RN6yVIlxIA2fTnz8fwdVWj2vTzLstfelsOj-VZlb6ioTTUNDmOMias-tLmQxzP6cB_QOaqwIWcE-NMGZxi-Lf2b0eS0Acg==; PC_TOKEN=bcacd0158d',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    params = {
        'is_new_segment':1,
        'fetch_hot':1
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_json(response):
    navList = np.append(response['groups'][3]['group'], response['groups'][4]['group'])
    #print(navList)
    for nav in navList:
        navName = nav['title']
        gid = nav['gid']
        containerid = nav['containerid']
        writerRow([navName,gid,containerid])

if __name__ == '__main__':
    init()
    url = 'https://www.weibo.com/ajax/feed/allGroups'
    parse_json(get_data(url))'''

import requests
import csv
import numpy as np
import os

def init():
    if not os.path.exists('./navData.csv'):
        with open('./navData.csv', 'w', encoding='utf-8',newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([
                'typeName',
                'gid',
                'containerid'
            ])

def writerRow(row):
    with open('./navData.csv', 'a', encoding='utf-8', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

def get_data(url):
    headers = {
        'Cookie':'SINAGLOBAL=4307542057500.3223.1717571699283; UOR=,,cn.bing.com; SCF=ApozugwcuzQLTGgRgQ6GbqqcZTMXtPWmcjnhBekgh2sSIrtOw0eDPyfjr3ZfWF87k5P_h1BQAU4b96esZdqBQGY.; SUB=_2A25LZvoRDeRhGeFH6VYU8yjEwj6IHXVoGnPZrDV8PUNbmtB-LU_4kW9Ne4t1NZuXdufD8Q-9G6YyRmpttc_2GBGh; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0OniMibjDQzvLY8zRHhpZ5JpX5o275NHD95QN1KzXSKec1h.EWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.ESh-0Son4entt; ALF=1718338790; ULV=1717740902982:4:4:4:3470754407274.255.1717740902964:1717731772022; XSRF-TOKEN=84icyK57B-GZziasnMHCF6b8; WBPSESS=XzliALnG2z6nsoGsiVOFCw7XVYw3h7QA4Fp3GZMxbVCWBbeQ9oPctzf5RN6yVIlxIA2fTnz8fwdVWj2vTzLstfelsOj-VZlb6ioTTUNDmOMias-tLmQxzP6cB_QOaqwIWcE-NMGZxi-Lf2b0eS0Acg==; PC_TOKEN=bcacd0158d',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    params = {
        'is_new_segment':1,
        'fetch_hot':1
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_json(response):
    navList = np.append(response['groups'][3]['group'], response['groups'][4]['group'])
    #print(navList)
    for nav in navList:
        navName = nav['title']
        gid = nav['gid']
        containerid = nav['containerid']
        writerRow([navName,gid,containerid])

if __name__ == '__main__':
    init()
    url = 'https://www.weibo.com/ajax/feed/allGroups'
    parse_json(get_data(url))