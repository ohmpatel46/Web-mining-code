import nltk
print("Enter 5 sentences: ")
b=[]
for i in range(0,5):
    a=input()
    b.append(nltk.word_tokenize(a))
print(b)
    