from flask import Flask,session,render_template,request,redirect,Blueprint
from utils.getHomePageData import *
from utils.getHotWordPageData import *
from utils.getPublicData import getAllHotWords
from snownlp import SnowNLP
pb = Blueprint('page',__name__,url_prefix='/page',template_folder='templates')

@pb.route('/home')
def home():
    username = session.get('username')
    articleLenMax,likeCountMaxAuthorName,cityMax = getTagsPageData()
    commentsListCountTopFore = getHomeCommentsLikeCountTopFore()
    xData,yData = getHomeArticleCreatedAtChart()
    typeChart = getHomeTypeChart()
    createAtChart = getHomeCommentCreateChart()
    return render_template('index.html',
                           username=username,
                           articleLenMax=articleLenMax,
                           likeCountMaxAuthorName=likeCountMaxAuthorName,
                           cityMax=cityMax,
                           commentsListCountTopFore=commentsListCountTopFore,
                           xData=xData,
                           yData=yData,
                           typeChart=typeChart,
                           createAtChart=createAtChart
                           )


@pb.route('/hotWord')
def hotWord():
    username = session.get('username')
    hotWordList = getAllHotWords()
    defaultHotWord  = hotWordList[0][0]
    if request.args.get('hotWord'):defaultHotWord = request.args.get('hotWord')
    hotWordLen = getHotWordLen(defaultHotWord)
    xData,yData = getHotWordPageCreatedAtCharData(defaultHotWord)
    sentences = ''
    value = SnowNLP(defaultHotWord).sentiments
    if value == 0.5:
        sentences = '中性'
    elif value > 0.5:
        sentences = '正面'
    elif value < 0.5:
        sentences = '负面'
    return render_template('hotWord.html',
                           username=username,
                           hotWordList=hotWordList,
                           defaultHotWord=defaultHotWord,
                           hotWordLen=hotWordLen,
                           sentences=sentences,
                           xData=xData,
                           yData=yData,
                           )


