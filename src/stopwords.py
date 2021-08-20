a=input("Enter your Sentence : ")
c=[',','.','?','\"','!']
stopwords=['.',',','a','they','the','his','so','and','were','from','that','of','in','only','with','to']
for j in c:
    x=' '+j
    a=a.replace(j,x)
b=a.split(' ')
d=[t for t in b if t not in stopwords]
print(d)