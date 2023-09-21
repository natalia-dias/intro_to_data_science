import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 8)

# Part 1: reading CSV

df_general = pd.read_csv('test/general.csv')
df_prenatal = pd.read_csv('test/prenatal.csv')
df_sports = pd.read_csv('test/sports.csv')
df_list = [df_general, df_prenatal, df_sports]

# Part 2: renaming columns and dropping useless column 'Unnamed'

df_sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
df_prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)

new_df = pd.concat([df_general, df_prenatal, df_sports], ignore_index=True)
new_df.drop(columns=['Unnamed: 0'], inplace=True)

# Part 3, handling missing values

new_df.dropna(axis=0, how='all', inplace=True)

new_df['gender'] = new_df['gender'].replace({'female': 'f', 'male': 'm', 'woman': 'f', 'man': 'm'})
new_df['gender'] = new_df.groupby(new_df['hospital'] == 'prenatal')['gender'].fillna('f')

zero_list = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
for col in new_df.columns:
    if col in zero_list:
        new_df[col].fillna(0, inplace=True)


# print(new_df.columns)

# Part 4, working with statistic

#answer_1
# Можно ли по-другому напрямую из запроса доставать ответ?
x = new_df['hospital'].value_counts()  # Which hospital has the highest number of patients?

for i in x.index:
    if x[i] == x.max():
        answer_1 = i

#answer_2
gen_hosp = new_df.where((new_df['hospital'] == 'general')).dropna(how='all')
gen_hosp_stomach = gen_hosp.where(gen_hosp['diagnosis'] == 'stomach').dropna(how='all')

answer_2 = (round(gen_hosp_stomach.shape[0] / gen_hosp.shape[0], 3))

# answer_3
sports_hosp = new_df.where((new_df['hospital'] == 'sports')).dropna(how='all')
sports_hosp_disloc = sports_hosp.where(sports_hosp['diagnosis'] == 'dislocation').dropna(how='all')

answer_3 = (round(sports_hosp_disloc.shape[0] / sports_hosp.shape[0], 3))

# answer_4

sport_hosp_age = sports_hosp['age'].agg('median')
answer_4 = gen_hosp['age'].agg('median') - sports_hosp['age'].agg('median')

# answer_5

prenat_hosp = new_df.where((new_df['hospital'] == 'prenatal')).dropna(how='all')

prenat_hosp_blood = prenat_hosp['blood_test'].value_counts()  #  другие варианты кроме как посмотреть на результаты?
# print(prenat_hosp_blood)
# gen_hosp['blood_test'].value_counts()


# print((f'''The answer to the 1st question is {answer_1}
# The answer to the 2nd question is {answer_2}
# The answer to the 3rd question is {answer_3}
# The answer to the 4th question is {answer_4}
# The answer to the 5th question is prenatal, 325 blood test'''))

# Part 5: visualization

# question 1: What is the most common age of a patient among all hospitals?

# print(new_df.age.agg('mode'))
bins = [0, 15, 35, 55, 70, 80]
plt.hist(new_df.age, bins=bins)
plt.show()

# question 2: What is the most common diagnosis among patients in all hospitals?

data = new_df.groupby('diagnosis').agg({'diagnosis': 'value_counts'})

diagnosis_list = []
labels = []
diagnosis_dict = data.to_dict()
for i in diagnosis_dict.values():
    for key, value in i.items():
        labels.append(key)
        diagnosis_list.append(value)

plt.pie(diagnosis_list, labels=labels)
plt.show()

# question 3: What is the main reason for the gap in values?

height_list = [gen_hosp['height'], sports_hosp['height'], prenat_hosp['height']]
fig, axes = plt.subplots()
plt.violinplot(height_list)
axes.set_xticks((1, 2, 3))
axes.set_xticklabels(('General', "Sports", "Prenatal"))
axes.set_ylabel("Height in meters")
plt.show()


print('''The answer to the 1st question: 15-35
The answer to the 2nd question: pregnancy
The answer to the 3rd question: It's because where is difference in units of measurement of height''')