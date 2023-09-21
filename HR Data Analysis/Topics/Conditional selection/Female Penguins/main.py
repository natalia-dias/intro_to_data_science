# your code here, the DataFrame is already loaded as penguins_df.
selecting_task = penguins_df.where(penguins_df['sex'] == 'FEMALE').dropna(how='all')

print(selecting_task)
