#creating a numpy sales report



import numpy as np

np.random.seed(seed=42)
sales_data_1d = np.random.randint(low =75, high = 200, size = 12) #1d  references its a a 1 dimensional array

print(f'Here is our sales data in 1D: \n{sales_data_1d}')

sales_data_2d = sales_data_1d.reshape(4, 3) #reshaping the 1d array into a 2d array with 4 rows and 3 columns

print(f'\nHere is our sales data in 2D: \n{sales_data_2d}')

