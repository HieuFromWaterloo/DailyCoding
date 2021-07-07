# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
Compute Corr of 2 list:

"""
import pandas as pd
# import numpy as np

x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

df = pd.DataFrame({"phys": phys, "hist": hist})
print(df['phys'].corr(df['hist']), 3)
