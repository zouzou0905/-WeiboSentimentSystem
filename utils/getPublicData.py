from utils.query import query
import re
import  sys
import pandas as pd
sys.path.append('model')

def getAllCommentsData():
    commentsList = query('select * from comments',[],'select')
    return commentsList

def getAllArticleData():
    articleList = query('select * from article',[],'select')
    return articleList

def getAllHotWords():
    data = []
    df = pd.read_csv('./model/cipingTotal.csv',encoding='utf-8')
    for i in df.values:
        try:
            data.append([
                re.search('[\u4e00-\u9fa5]+',str(i)).group(),
                re.search('\d+',str(i)).group(),
            ])
        except:
            continue
    return data