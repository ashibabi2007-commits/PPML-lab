import pandas as pd
data= {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print("DataFrame :\n", df)
print("\nAge column :", df['Age'])
print("\nRow at index 1 :\n", df.iloc[1])