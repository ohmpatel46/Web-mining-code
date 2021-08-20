import nltk
print("Enter your paragraph: ")
a=input()
b=nltk.sent_tokenize(a)
print("\n\nSentence-wise tokenization of the paragraph:\n")
print(b)
c=nltk.word_tokenize(a)
print("\n\nWord-wise tokenization of the paragraph:\n")
print(c)