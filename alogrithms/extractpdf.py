import convertapi
convertapi.api_secret = '9JqSIe7fJPGuMHsh'
convertapi.convert('txt', {
    'File': 'Transcript.pdf'
}, from_format = 'pdf').save_files('Transcript.txt')
'''

def getinfo(key1,key2,key3):
    dic = {}
    linenum , res = 0 , 0
    lst = simplify('Demo Transcript1.txt')
    ls = len(lst)
    for ele in lst:
        if key1 in ele:
           break
        linenum += 1
    for i in range(linenum,ls):
        if key2 in lst[i]:
            dic[lst[i]] = float(lst[i+1])
    #res = sorted(dic.items(),key = lambda item : item[1],reverse = True)
    #return res[:key3]
    for key in dic:
        res += dic[key]
    res /= len(dic)
    return round(res,3)

def simplify(file):
    lst = []
    #f = open('Demo Transcript1.txt')
    with open(file,'r') as files:
    #content = f.readline()
        while True:
            line = files.readline()
            if not line:
                break
            line = line.replace('\n','')
            line = line.strip()
            if line:
                lst.append(line)
    return lst
sentiment_score = []

def get_score(text1):
    for text in text1:
        client = language.LanguageServiceClient()
        # The text to analyze
        document = types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment_score.append(client.analyze_sentiment(document=document).document_sentiment.score)

        # print('Text: {}'.format(tweet))   #debug
        # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))  #debug

    # average_sentiment = mean(sentiment_score_list)

    average_sentiment = sum(sentiment_score) / len(sentiment_score)
    return [average_sentiment, sentiment_score]


print(get_score(tweet1)[0])
'''

'''
#if "__name__" == "__main__":
print(simplify('Demo Transcript1.txt'))
print(getinfo('COURSES','ENG',3))
'''