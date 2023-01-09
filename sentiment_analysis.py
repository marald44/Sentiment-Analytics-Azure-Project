import pandas as pd
from itertools import zip_longest
import sys
sys.path.append('Text-Analytics')
from credentials import client
import csv

client = client()

#for iterating the document to divide them into chunks of 10
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

"""
Sentiment analysis & Opinion mining
"""
# Create a CSV file and write the header row
with open('sentiment_scores.csv', 'w', newline='') as csvfile:
    fieldnames = ['text', 'sentiment', 'confidence_scores']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

df = pd.read_csv("Womens Clothing E-Commerce Reviews.csv")
df_100 = df.head(100)

documents = []
for index, row in df_100.iterrows():
    documents.append({
        'id': str(index),
        'language': 'en',
        'text': row['Review Text']
    })


for documents_batch in grouper(documents, 10):
    documents_batch = [d for d in documents_batch if d is not None]
    response = client.analyze_sentiment(documents=documents_batch,show_opinion_mining=True)
    
    
    for item in response:
    
        txt = item.sentences[0]['text']
        sent = item.sentences[0]['sentiment']
        confidence = item.sentences[0]['confidence_scores']
        with open('sentiment_scores.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'text': txt, 'sentiment': sent, 'confidence_scores': confidence})
        #print(txt + sent + str(confidence) , end="\n--------------ENDING--------------\n")





        



