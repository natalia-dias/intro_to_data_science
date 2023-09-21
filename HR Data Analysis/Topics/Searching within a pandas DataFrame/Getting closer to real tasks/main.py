# your code here. the dataset is already loaded as sales_data.

print(sales_data.query("Sales < 25 & Category in ['Technology', 'Furniture']"))