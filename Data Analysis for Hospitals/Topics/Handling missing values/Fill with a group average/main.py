#  write your code here 
import pandas as pd

df = pd.read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Fill with a group average/data/dataset/input.txt')
# print(df.head(5))
# print(df.isna().sum())

# df['height'] = df.groupby('location')['height'].apply(lambda x: x.fillna(x.mean()))
# print(round(df.height.sum(), 1))
# av_height = df.groupby('location')['height'].mean()
# print(av_height)
df = df.groupby('location')['height'].apply(lambda x: x.fillna(x.mean())).reset_index().round(decimals=1)
print(df.height.sum())
