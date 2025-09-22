#Create a Series from a dict {'Math':90, 'Science':80, 'English':95} and print only the values greater than 85.
import pandas as  pd 
data={'Math': 90,'Science':80,'English':95}
d=pd.Series(data)
print(d[d>85])
