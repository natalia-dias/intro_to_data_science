#  write your code here
import pandas as pd

df = pd.read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Handle missing values/data/dataset/input.txt')

df = df.dropna(axis=1, thresh=13)
mode_price = df['price'].median()
df['price'].fillna(mode_price, inplace=True)

print(df.head(5))
