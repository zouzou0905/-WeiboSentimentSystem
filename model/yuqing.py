import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import csv
from utils.getPublicData import getAllCommentsData
from model.cutComments import main as cutCommentsMain
from cipingTotal import main as ciPingTotalMain
import os

# Load and prepare training data
data = pd.read_csv('cutComments.txt')
X_train, X_test, y_train, y_test = train_test_split(data['comment'], data['label'], test_size=0.2, random_state=42)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

def analyze_sentiment(comment):
    comment_vec = vectorizer.transform([comment])
    prediction = clf.predict(comment_vec)
    return prediction[0]

def targetFile():
    targetFile = 'target.csv'
    commentList = getAllCommentsData()

    rateData = []
    good = 0
    bad = 0
    midlle = 0
    for index, i in enumerate(commentList):
        try:
            sentiment = analyze_sentiment(i[4])
            if sentiment == 'positive':
                good += 1
                rateData.append([i[4], '正面'])
            elif sentiment == 'neutral':
                midlle += 1
                rateData.append([i[4], '中性'])
            elif sentiment == 'negative':
                bad += 1
                rateData.append([i[4], '负面'])
        except:
            continue

    for i in rateData:
        with open(targetFile, 'a+', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(i)
    with open(targetFile, 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([good, midlle, bad])

def main():
    try:
        os.remove('./target.csv')
        os.remove("./cutComments.txt")
        os.remove("./cipingTotal.csv")
    except:
        pass
    cutCommentsMain()
    ciPingTotalMain()
    targetFile()

if __name__ == '__main__':
    main()
