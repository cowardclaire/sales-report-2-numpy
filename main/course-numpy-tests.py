
import numpy as np

macro_arr=np.array([[513850, 0.4, 0.5],[516876, 0.3, 0.5],[518915, 0.4, 0.5],[521920, 0.4, 0.5],[523813, 0.7, 0.5],[526750, 0.7, 0.5],[528712, 1.0, 0.25],[532082, 1.5, 0.25]])
print(macro_arr[:,0])

gdp_arr = macro_arr[0:4,0]
sum_gdp_arr = np.sum(gdp_arr)
print("Sum of GDP array:", sum_gdp_arr)

cpi_arr = macro_arr[:,1]
bank_rate_arr = macro_arr[:,2]  

interest_rate_arr = bank_rate_arr - cpi_arr
print("Interest Rate Array:", interest_rate_arr)

mean_2nd_3rd_col_arr = macro_arr[:,1:3]
mean_values = np.mean(mean_2nd_3rd_col_arr, axis=0)
print(mean_values)

std_2nd_3rd_col_arr = macro_arr[:,1:3]
std_values = np.std(std_2nd_3rd_col_arr, axis=0)
print(std_values)
