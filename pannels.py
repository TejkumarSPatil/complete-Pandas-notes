####            PANEL

* A panel is a 3D container of data. The term Panel data is derived from 
   econometrics and is partially responsible for the name pandas − pan(el)-da(ta)-s.
   
* The names for the 3 axes are intended to give some semantic meaning to 
    describing operations involving panel data. They are −

      > items − axis 0, each item corresponds to a DataFrame contained inside.
      > major_axis − axis 1, it is the index (rows) of each of the DataFrames.
      > minor_axis − axis 2, it is the columns of each of the DataFrames.
    
Create Panel-
      A Panel can be created using multiple ways like −
           * From ndarrays
           * From dict of 

 #####  Create an Empty Panel
import pandas as pd
p=pd.Panel()
print(p)

import pandas as pd
p=np.random.rand(2,4,6)
df=pd.Panel(p)
print(df)

##  From 3D ndarray
import pandas as pd
import numpy as np
data=np.random.rand(4,5,6)
p=pd.Panel(data)
print(p)

#########   From dict of DataFrame Objects

import pandas as pd
import numpy as np
data={'item1':pd.DataFrame(np.random.rand(2,3)),
      'item2':pd.DataFrame(np.random.rand(4,6))}
p=pd.Panel(data)
print(p)

print(p['item1'])
print(p['item2'])


print(p.major_xs(1))
print(p.minor_xs(1))

###  p.axes
###  p.items
###  p.major_axis
###  p.minor_axis
###  p.ndim   o/p is 3 (3 dimensions)
###  p.dtypes
###  p.shape  o/p is (2,4,6) 
            # here,  2=num of items
            #        4=major axis(comparing two items which one is larger)
            #        6=minor axis(comparing two items which one is larger)
            
###  p.size   o/p is 48 ie,(2*4*6)
###  p.values            


 

































