#  write your code here 
import pandas as pd

df = pd.read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Guess the meaningful replacement/data/dataset/input.txt')
df_total_space = df.livingsp + df.nonlivingsp
df['totsp'].fillna(df_total_space, inplace=True)
print(int(df['totsp'].sum()))
