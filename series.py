#  import the pandas library and aliasing as pd

import pandas as pd
s1=pd.Series()
print(s1)   

#import the pandas library and aliasing as pd
import pandas as pd
data=(['aa',45,'bb','cc'])
s1=pd.Series(data)
print(s1)     ###   here no index is passed
## s1[0]
## s1[:2]
## s1[2:]
## s1[:-2]
## s1[-2:]

import pandas as pd
data=(['aa',45,'bb','cc'])
s1=pd.Series(data,index=['apple','mango','orange','pappaya'])
print(s1)
## s1['apple']
## s1[['apple','mango']]
## s1[['apple','mango','orange']]

##  create a series from dictionary

import pandas as pd
dict={'name':['fv','a'],'age':[334,56]}
s=pd.Series(dict)
print(s)


import pandas as pd
dict={'a':1,'b':2,'c':3,'d':4}
s1=pd.Series(dict)
print(s1)  ### here no index is required

import pandas as pd
dict={'a':1,'b':2,'c':3,'d':4}
s1=pd.Series(dict,index=['a','b','c','d','f'])
print(s1)

import pandas as pd
dict={'a':1,'b':2,'c':3,'d':4}
s1=pd.Series(dict,index=['b','c','a','f','d'])
print(s1) ###  If index is passed, the values in data corresponding to the labels in the index will be pulled out.

####     Create a Series from Scalar
## If data is a scalar value, an index must be provided. The value will be repeated to match the length of index
import pandas as pd
s1=pd.Series(5,index=[1,2,3,4,5,6])
print(s1)
























