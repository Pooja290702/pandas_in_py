import pandas as pd 
df={'city':['a','b','c','d','e','f'],'product':['q','w','e','r','t','y'],'sales':[10,20,30,40,50,60]}
a=pd.DataFrame(df)
grouped=a.groupby('city')['sales'].agg(['mean','max'])
print(grouped)
