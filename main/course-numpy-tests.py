#array course test,  Finish the following line of code to create this 1D list: We have quarterly UK MacroData years 2000-2023, and we want to use GDP values for the year 2022:

[567396, 567889, 567445, 568034]

import numpy as np

mylist = [567396, 567889, 567445, 568034]
mylist_array = np.array(mylist)

print(mylist_array)

for value in mylist_array:
    if value > 567500:
        print(f'This value is greater than 567500: {value}')