import urllib.request
import nltk
from bs4 import BeautifulSoup
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read().decode('utf8')
h=nltk.word_tokenize(html)
print("The tokens without removing html tags:\n\n",h[:200]) #Only displaying 200 tokens for convinience
raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = nltk.word_tokenize(raw)
print("\n \n \nThe tokens after removing HTML tags:\n\n",tokens[:200]) #Only displaying 200 tokens for convinience