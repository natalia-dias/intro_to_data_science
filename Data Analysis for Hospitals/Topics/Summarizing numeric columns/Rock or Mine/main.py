#  write your code here
import pandas as pd

df_rock = pd.read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Summarizing numeric columns/Rock or Mine/data/dataset/input.txt')

median_rock = df_rock.where(df_rock.labels == 'R').dropna(how='all')
median_mine = df_rock.where(df_rock.labels == 'M').dropna(how='all')
print(f'M = {round(median_mine.null_deg.median(), 3)} R = {round(median_rock.null_deg.median(), 3)}')
