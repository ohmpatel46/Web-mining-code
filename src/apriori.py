import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
dataset = pd.read_csv('data.csv', header = None)
transactions = []
for i in range(0, 9):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 4)])
rules = apriori(transactions, min_support = 0.222, min_confidence = 0.777, min_lift = 3, min_length = 2)
results = list(rules)
print(results)
for i in results:
    print(i)