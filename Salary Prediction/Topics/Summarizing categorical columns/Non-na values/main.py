#  write your code here
import pandas as pd


df_rock = pd.read_csv('/Users/ndias/PycharmProjects/Salary Prediction/Topics/Summarizing categorical columns/Non-na values/data/dataset/input.txt')
shape = df_rock.shape
# print(shape[0])
# y = df_rock.labels.shape
x = df_rock['labels'].isna().sum()
# print(x)
print(shape[0] - x)
