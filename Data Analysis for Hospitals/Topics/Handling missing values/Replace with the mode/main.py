#  write your code here 
import pandas as pd

df = pd.read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Handling missing values/Replace with the mode/data/dataset/input.txt')

df_loc = df['location'].mode()[0]
df['location'].fillna(df_loc, inplace=True)

# print(df.head(5))

print(df['location'].mode())