a=input("Enter your Sentence\n\n")
c=[',','.','?','\"','!']
for j in c: 
    x=' '+j
    a=a.replace(j,x)
b=a.split(" ")
print("\n\n")
print(b)
