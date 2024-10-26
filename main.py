#importing pandas
import pandas as pd
#importing matplotlib
import matplotlib.pyplot as plt
#connecting with file
data=pd.read_csv("Countries Data.csv")

cyear1952=data.loc[data['year']==1952]

#now finding for 2007
cyear2007=data.loc[data['year']==2007]

#merging
cmerge=cyear1952.merge(cyear2007,right_on='country',left_on='country')

cmerge.drop(['year_x','year_y'],axis=1)
print(cmerge.head())
cmerge['population_growth']=cmerge['population_y']-cmerge['population_x']
cmerge.sort_values('population_growth',ascending=False)
print(cmerge.info(10))
plt.bar(cmerge['country'],cmerge['population_growth'],color='maroon',width=0.5)
plt.show()
