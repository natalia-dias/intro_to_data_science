# your code here. the dataset is already loaded as food_calories_df.
check_list = ['CARROTS,RAW', 'BREAD,WHEAT', 'CRANBERRIES,RAW', 'SUGARS,MAPLE', 'WATER,TAP,WELL']
# print(food_calories_df[food_calories_df.Shrt_Desc.isin(check_list)].Energ_Kcal.agg('sum'))
print(food_calories_df.query('Shrt_Desc.isin(@check_list)').Energ_Kcal.agg('sum'))