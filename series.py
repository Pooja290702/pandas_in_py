#series is like a column in a table, it is one dimensional
import pandas as pd
a=[1,2,3,4]
my_series=pd.Series(a,index=['a','b','c','d'])
print(my_series)
