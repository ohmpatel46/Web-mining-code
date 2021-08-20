a=input("Enter your Paragraph:\n")
b=[]
d=[]
y=a.split('.')
c=[',','.','?','\"','!']
for i in range(len(y)):
    b.append(y[i])
    d.append(b[i].split(" "))
print("Sentence-wise tokenisation:\n")
print(b)
print("\nWord-eise tokenisation:\n")
print(d)

