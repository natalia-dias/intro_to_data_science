#  write your code here 
import pandas as pd

df = pd.read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Working with missing values/Drop NaNs/data/dataset/input.txt')
x = df.shape[0]
df.dropna(axis=0, inplace=True)
y = df.shape[0]

print(x, y)
