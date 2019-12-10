import cloudconvert
from gensim.summarization import keywords
import warnings
import pandas as pd
consumer_key = 'OPXVWM0pzdkiOWzvwZKwNjffb'
consumer_secret = '0PlU0H4wLc6bh7Q0GAZN2ms3Tf6a6aQCTRkj7GybBWOoL4yyUH'
access_key = '1171846283398537216-Bw08bbT7jg7HhjeiYu1YrWLUeeJp2F'
access_secret = '3ynyTQPgsLL2KXqgKZ7VmZ0sZL408PNAClIrtHQiETtHh'
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#import numpy as np
#import PyPDF2
#import textract
import re
def simplify(file):
    lst = []
    str = ""
    #f = open('Demo Transcript1.txt')
    with open(file,'r') as files:
    #content = f.readline()
        while True:
            line = files.readline()
            if not line:
                break
            line = line.replace('\n','')
            line.encode('utf-8').strip()
            if line:
                lst.append(line)
    for i in lst:
        str += ' ' + i
    return str
def Keyword_Extract(file,key):
        '''
        filename = file

        pdfFileObj = open(filename, 'rb')  # open allows you to read the file
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # The pdfReader variable is a readable object that will be parsed
        num_pages = pdfReader.numPages  # discerning the number of pages will allow us to parse through all the pages

        count = 0
        text = ""

        while count < num_pages:  # The while loop will read each page
            pageObj = pdfReader.getPage(count)
            count += 1
            text += pageObj.extractText()

        # Below if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.

        if text != "":
            text = text

        # If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text

        else:
            text = textract.process('http://bit.ly/epo_keyword_extraction_document', method='tesseract', language='eng')
        text = text.encode('ascii', 'ignore').lower()  # Lowercasing each word
        print(text)
        '''
            # Now we have a text variable which contains all the text derived from our PDF file.
        text = simplify(file)
        warnings.filterwarnings("ignore")
        values = keywords(text=text,split='.',scores=True)
        data = pd.DataFrame(values,columns=['keyword','score'])
        data = data.sort_values('score',ascending=False)
        return data.head(key)
print(Keyword_Extract('test2.txt',20))
def detials(file):
    lst = []
    text = simplify(file)
    pattern = r',|;|\?|\.|\:'
    res = re.split(pattern,text)
    Keyword = ['like','good at','strong','better','specilize','speciliazing','curious','interest','interested','research','intern','goals','targets','skill']
    for i in res:
        for t in Keyword:
            if t in i:
                lst.append(i)
    for ele in lst:
        print(ele)


'''
api = cloudconvert.Api("5jahP1MXvASNf6nqMdctxIxbxKa9Dl4FrMwVruGQYCbhtAtUdE5WrSOX1MwNenju")
process = api.createProcess({
    "inputformat": "pdf",
    "outputformat": "txt"
})
process = api.convert({
    "inputformat": "pdf",
    "outputformat": "txt",
    "input": "upload",
    "file": open('test2.pdf', 'rb')
})
process.wait()
process.download()
'''

'''
    pattern = r',|;|\?|\.|\:'
    res = re.split(pattern,str)
    return res
'''
#print(simplify('test2.txt'))
detials('test2.txt')
'''
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

text1 = simplify('test2.txt')
print(get_score(text1)[0])

'''