import pandas as pd

penguin_sample = {'species': {0: 'Adelie', 1: 'Adelie', 2: 'Gentoo', 3: 'Gentoo', 4: 'Adelie',
                              5: 'Adelie', 6: 'Adelie', 7: 'Gentoo', 8: 'Gentoo', 9: 'Adelie', 10: 'Adelie',
                              11: 'Adelie', 12: 'Adelie', 13: 'Adelie', 14: 'Gentoo', 15: 'Adelie', 16: 'Adelie',
                              17: 'Adelie', 18: 'Adelie', 19: 'Adelie'},
                  'sex': {0: 'FEMALE', 1: 'FEMALE', 2: 'FEMALE', 3: 'MALE', 4: 'FEMALE', 5: 'MALE',
                          6: 'MALE', 7: 'MALE', 8: 'MALE', 9: 'MALE', 10: 'FEMALE', 11: 'FEMALE', 12: 'FEMALE',
                          13: 'MALE', 14: 'FEMALE', 15: 'FEMALE', 16: 'FEMALE', 17: 'MALE', 18: 'FEMALE',
                          19: 'MALE'}}

df = pd.DataFrame(penguin_sample)

# your code here
print(df.groupby('sex').agg({'species': 'count'}))
