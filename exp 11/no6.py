import pandas as pd
data = [10,20,30]
labels = ['a','b','c']
series = pd.Series(data, index= labels)
print("Pandas series :\n", series)
print("Value at label 'b':", series['b'])