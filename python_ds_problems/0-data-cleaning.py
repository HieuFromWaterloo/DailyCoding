# >>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> Q1 <<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>

import re

x = "123-456-789"

# check if x is a valid phone number
print(bool(re.compile("\d{3}-\d{3}-\d{4}").match(x)))

# >>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> Q2 <<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>

"""
customers_df
  customer_id order_id
0        32         21
1        34         22
2        13         23
3        12         24

employees_df
  employee_id   name
0          31   Nick
1          32   Lore
2          33 Martin
3          34     Jo

Output:
customer_id  order_id  employee_id  name
0           32        21           32  Lore
1           34        22           34    Jo
"""
import pandas as pd

pd.merge(left=customers_df, right=employees_df,
         left_on="customer_id", right_on="employee_id")

# >>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> Q3 <<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>

"""
Which is NOT tidy and why?

df1.head()
   Ozone  Solar.R  Month  Day
0   41.0    190.0      5    1
1   36.0    118.0      5    2
2   12.0    149.0      5    3
3   18.0    313.0      5    4
4    NaN      NaN      5    5
...

df2.head() ---> answer: this one because each variable is not a separate column
   Month  Day variable  value
0      5    1    Ozone   41.0
1      5    2    Ozone   36.0
2      5    3    Ozone   12.0
3      5    4    Ozone   18.0
4      5    5    Ozone    NaN
...
"""


# >>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> Q4 <<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>

"""
class     name  test1  test2
0      1     Nick     11     32
1      2    Sarah     12     45
2      1  Jasmine     92     62
3      2   Martin     56     34

expected output:

       test1  test2
class
1       51.5   47.0
2       34.0   39.5
"""

pd.pivot_table(index="class")

df["A"].value_counts()
"""
colA | count
a | 2
b | 3
c | 1
"""

# >>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> Q5 <<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>

"""
eggs  salt  spam
month
jan      47  12.0    17
feb     110  50.0    31
mar     221  89.0    72
apr      77  87.0    20
may     132   0.0    52
jun     205  60.0    55

Expected output:

        eggs    ...            new
month          ...
jan      47    ...      not equal
feb     110    ...      not equal
mar     221    ...      not equal
apr      77    ...      not equal
may     132    ...      not equal
jun     205    ...      not equal
"""

df = init_df()
mapper = {True: 'equal', False: 'not equal'}
df['new'] = (df['salt'] == 30).map(mapper)
print(df)

"""
        eggs  salt  spam
month
jan      47  12.0    17
feb     110  50.0    31
mar     221  89.0    72
apr      77  87.0    20
may     132  [0.0]  52 --- return this [...]
jun     205  60.0    55
"""
df.loc["may", "salt"]


# note: correct way to select "age" ROW and "name" COL
df[col][row]


# >>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>> Q6 <<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>

"""
        eggs  salt  spam
month
jan      47  12.0    17
feb     110  50.0    31
mar     221  89.0    72
apr      77  87.0    20
may     132  0.0     52
jun     205  60.0    55

Expected output #1:
        eggs  salt  spam
month
jan      47  12.0    17
feb     110  50.0    31
mar     [300]  89.0    72
apr      77  87.0    20
may     132  0.0     52
jun     205  60.0    55

Expected output #2:
       eggs  ...   spam
month        ...
jan      47  ...     17
feb     110  ...     31
mar     221  ...     72
apr      77  ...     20
may     132  ...     52
"""

# Expected output #1
df.eggs[df.spam > 65] = 300

# Expected output #2
df.apply(lambda n: n // 4)
