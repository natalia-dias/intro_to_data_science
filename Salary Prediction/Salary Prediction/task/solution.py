# import os
# import requests

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error as mape

# # checking ../Data directory presence
# if not os.path.exists('../Data'):
#     os.mkdir('../Data')
#
# # download data if it is unavailable
# if 'data.csv' not in os.listdir('../Data'):
#     url = "https://www.dropbox.com/s/3cml50uv7zm46ly/data.csv?dl=1"
#     r = requests.get(url, allow_redirects=True)
#     open('../Data/data.csv', 'wb').write(r.content)

# read data
# data = pd.read_csv('/Users/ndias/PycharmProjects/Salary Prediction/Salary Prediction/Data/data.csv')
# corr = data.corr()
# plt.imshow(corr)


# print(data.head())
# write your code here
# # print(data[['rating']].head(5))
# # print('____')
# y = data['salary']
# X = data.drop(columns='salary')
# # print(X.head())
# #
# # # print(X.head(5))
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mod_coef = [str(i) for i in model.coef_]
# print(', '.join(mod_coef))
# intercept = round(model.intercept_, 5)
# slope = model.coef_
# mape_score = mape(y_test, y_pred)
# print(round(mape_score, 5))
# power_2 = 1.0414
# power_3 = 0.94182
# power_4 = 1.07652
# # print(intercept, round(slope[0], 5), round(mape_score, 5))
# print(power_3)

def fit_without_corr(data_x):
    corr_vars = ['rating', 'age', 'experience']
    mape_score_list = []
    for i in range(3):
        data_copy = data_x.copy()
        y = data_copy['salary']
        columns = corr_vars[i]
        X = data_copy.drop(columns=columns)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mape_score = (round(mape(y_test, y_pred), 5))
        mape_score_list.append(mape_score)
        print(f'Test {i}, data without {corr_vars[i]}, mape score is {mape_score}')
    return mape_score_list


def fit_without_double_corr(data_x):
    corr_vars = [['rating', 'age'], ['experience', 'rating'], ['experience', 'age']]
    mape_score_list = []
    for i in range(3):
        data_copy = data_x.copy()
        y = data_copy['salary']
        columns = corr_vars[i]
        X = data_copy.drop(columns=columns)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mape_score = (round(mape(y_test, y_pred), 5))
        mape_score_list.append(mape_score)
        print(f'Test {i}, data without {corr_vars[i]}, mape score is {mape_score}.')
    return mape_score_list


# one_corr = fit_without_corr(data)
# double_corr = fit_without_double_corr(data)
# fit_without_corr(data)

# print(0.94701)



