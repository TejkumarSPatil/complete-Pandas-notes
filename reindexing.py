############   REINDEXING  ##############

import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
df1 = df1.reindex_like(df2)
print(df1)

#################################################################
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
df2 = df2.reindex_like(df1)
print(df2)

##  np.mean(df2['col1'])
##  np.mean(df2['col2'])

##  df2.fillna(np.mean(df2['col1']))
##  df2.fillna(np.mean(df2['col2']))

df1['c1']=df1['c1'].fillna(df1['c1'].mean())


##  df2.dropna()  o/p is all NaN are removed

# mean value of col1,col2,col3
df2.fillna({'col1':-0.8725724016176745,'col2':-0.4089452099728668,'col3':0.32268828394786164})
df2.fillna({'col1':0.5384176720320875,'col2':-0.4089452099728668})


# df2.fillna(method='ffill')   ffill=forward fill  (in the NaN places enter the previous value )
# df2.fillna(method='bfill')   bfill=backward fill
# df2.fillna(method='bfill',axis='columns')    axis=it copies the value from neighbour(side)
# df2.fillna(method='ffill',limit=1)      (in the NaN places enter the previous first value)
#  df2.fillna(method='ffill',limit=1)      (in the NaN places enter the previous first value)

##  del df2['col3']
##  press df2

##  df2.drop(6)     deleting rows

##  df2.fillna(method="pad")     6th row values shift to 7th row den 7th row values goes to 8th row



















