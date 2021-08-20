import warnings
import nltk
import bs4 as bs
import urllib.request
import re

corpus=[]
docs=[]
for i in range(3):
    print("Enter the URL of the page to be inspected: ")
    url=input()
    raw_html = urllib.request.urlopen(url)
    raw_html = raw_html.read()
    
    article_html = bs.BeautifulSoup(raw_html, 'lxml')
    
    article_paragraphs = article_html.find_all('p')
    
    article_text = ''
    
    for para in article_paragraphs:
        article_text += para.text
    
    corpus.append(nltk.sent_tokenize(article_text))
    text=''
    for j in range(len(corpus[i] )):
        corpus [i][j] = corpus[i][j].lower()
        corpus [i][j] = re.sub(r'\W',' ',corpus[i][j])
        corpus [i][j] = re.sub(r'\s+',' ',corpus[i][j])
        text=text+corpus[i][j]
    docs.append(text)

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
from sklearn.feature_extraction.text import TfidfVectorizer

print("\n\n The TF/IDF matrix is:\n\n")
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
print(tfidf_matrix)

from sklearn.metrics.pairwise import cosine_similarity
print("\n\n The cosine similarity matries are:\n\n")

#This will print out the cosine similarity WRT Each of the website's corpus one by one. Therefore it has 3 columns.
print(cosine_similarity(tfidf_matrix[0:3], tfidf_matrix))

