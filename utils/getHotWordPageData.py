from utils.getPublicData import *

def getHotWordLen(hotWord):
    commentsList = getAllCommentsData()
    hotWordLen = 179
    for comment in commentsList:

        if comment[4].find('hotWord') != -1:
            hotWordLen += 1
    return hotWordLen

def getHotWordPageCreatedAtCharData(hotWord):
    commentsList = getAllCommentsData()
    createdAt = {}
    for i in commentsList:
        if i[4].find('hotWord') != -1:
            if createdAt.get(i[1],-1)==-1:
                createdAt[i[1]] = i
            else:
                createdAt[i[1]] += 1
    return list(createdAt.keys()),list(createdAt.values())