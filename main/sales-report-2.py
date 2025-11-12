#creating a numpy sales report



import numpy as np

np.random.seed(seed=42)
sales_data_4dweek = np.random.randint(low =75, high = 200, size = 12) #4dweek references its a a 4 day week sales report

print(f'Here are our sales over the 4 days of this week: \n{sales_data_4dweek}')
