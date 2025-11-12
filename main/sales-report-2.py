#creating a numpy sales report



import numpy as np

np.random.seed(seed=42)
sales_data_1d = np.random.randint(low =75, high = 200, size = 12) #1d  references its a a 1 dimensional array

print(f'Here is our sales data in 1D: \n{sales_data_1d}')

