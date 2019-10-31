A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

Features of DataFrame:
    
> Potentially columns are of different types
> Size – Mutable
> Labeled axes (rows and columns)
> Can Perform Arithmetic operations on rows and columns

Create DataFrame:
A pandas DataFrame can be created using various inputs like −
. Lists
. dict
. Series
. Numpy ndarrays
. Another 

ASSIGNMENTS
1.HOW TO ADD EXTRA ELEMENT TO THE LIST
2.IF WE APPENDING NUM SHOULD BE CONTINOUS LIKE 1 2 3 4 5 6 ......

import pandas as pd
df=pd.DataFrame()
print(df)

###   Create a DataFrame from Lists
import pandas as pd
data=([100,200,300,400,500])
df=pd.DataFrame(data)
print(df)
##################################### append
import pandas as pd
data=([100,200,300,400,500])
df=pd.DataFrame(data)
print(df)

data1=([100,200,300,400,500,600])
df1=pd.DataFrame(data1)
print(df1)

df=df.append(df1,ignore_index=True) # very very imp
print(df)



#############################################
import pandas as pd
data=([['aaa',20],['bbb',30],['ccc',40]])
df=pd.DataFrame(data)
print(df)

import pandas as pd
data=([['aaa',20],['bbb',30],['ccc',40]])
df=pd.DataFrame(data,index=['ram','asd','hgf'])
print(df)

import pandas as pd
data=([['aaa',20,100],['bbb',30,200],['ccc',40,300]])
df=pd.DataFrame(data,index=['ram','asd','hgf'],columns=['name','age','scores'],dtype=float)
print(df)

for index,row in df.iterrows():  # iterrating over rows
    print(index,row)

df[df['name'].isin(['bbb'])]   # getting bbb information
# for values  df[df['age'].isin([30])] 
 
 
 
 
 
 
################################################# append
import pandas as pd
data=([['aaa',20],['bbb',30],['ccc',40]])
df=pd.DataFrame(data,index=['ram','asd','hgf'],columns=['name','age'])
print(df)

data1=([['xxx',20],['yyy',30],['zzz',40]])
df1=pd.DataFrame(data,index=['rbh','jsd','lzz'],columns=['name','age'])
print(df1)

df=df.append(df1)
print(df)

###   df.drop('lzz')  ##  very tmp


import pandas as pd
data=([['aaa',20],['bbb',30],['ccc',40]])
df=pd.DataFrame(data,index=['ram','asd','hgf'],columns=['name','age'],dtype=float)
print(df)

##   Create a DataFrame from Dict of ndarrays / Lists

import pandas as pd     # very very important
employ_info={'surya':['surya@gmail.com',123],'ganesh':['ganesh@gmail.com',456]}

employ_info['surya']
employ_info['surya'][0]
employ_info['surya'][1]
employ_info.keys()
employ_info.values()

df=pd.DataFrame(employ_info)
print(df)





import pandas as pd
dict={'name':['aaa','bbb','ccc','ddd'],'age':[12,23,34,45]}
df=pd.DataFrame(dict)
print(df)

import pandas as pd
dict=({'name':['aaa','bbb','ccc','ddd'],'age':[12,23,34,45]})
df=pd.DataFrame(dict,index=['A','B','C','D'])
print(df)

import pandas as pd
dict=({'name':['aaa','bbb','ccc','ddd'],'age':[12,23,34,45]})
df=pd.DataFrame(dict,index=['A','B','C','D'])
print(df)

###   Create a DataFrame from List of Dicts
import pandas as pd
list=[{'a':1,'b':2,'c':3},{'d':4,'e':5,'f':6,'g':7}]
df=pd.DataFrame(list)
print(df)

import pandas as pd
dict=[{'a':1,'b':2,'c':3},{'d':4,'e':5,'f':6,'g':7}]
df=pd.DataFrame(dict,index=['tej','ram'])
print(df)

import pandas as pd
dict=[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6,'g':7}]
df=pd.DataFrame(dict,index=['tej','ram'])
print(df)

##  create a DataFrame with a list of dictionaries, row indices, and column indices.
import pandas as pd
dict=[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6,'g':7}]
df=pd.DataFrame(dict,index=['tej','ram'],columns=['a','b'])
print(df)

import pandas as pd
dict=[{'a':1,'b':2,'c':3},{'a':4,'b':5,'c':6,'g':7}]
df=pd.DataFrame(dict,index=['tej','ram'],columns=['a','b','g'])
print(df)

##  Create a DataFrame from Dict of Series
import pandas as pd
dic={'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['d','e','f','g'])}
df=pd.DataFrame(dic)
print(df)

import pandas as pd
dic={'one':pd.Series([1,2,3],index=['a','b','c']),
     'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df=pd.DataFrame(dic)
print(df)
##  df['one']
##  df['two']
##  df[0:2]        very very imp

############  adding new column
import pandas as pd
list=[3,5,34,56,33,5]
df=pd.DataFrame(list)
print(df)

df[1]=pd.DataFrame([32,45,53,22,4])
print(df)

df['sum']=df[0] + df[1]  # adding two columns
print(df)

#######################

import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

df['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df)

import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

df['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df)

df['four']=pd.Series([11,12,34,34],index=['a','b','c','d'])
print(df)

##########  adding any two columns  
df['four']=df['two']+df['one']
print(df)

#################  deletion of columns
import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
      'three':pd.Series([10,20,30],index=['a','b','c'])}
df = pd.DataFrame(d)
print(df)  

print(df[2:4])  ## slicing of rows
                      
## del df['one']  Deleting the first column using DEL function:
## df

## df.pop('one')  Deleting another column using POP function:
## df

## df.pop('two')
## df

## df.loc['b']   Selection by Label

## df.iloc[2]  Selection by integer location

##########  Addition of Rows
import pandas as pd
data = [['Alex',10,'m'],['ruby',20,'f'],['Spark',30,'m'],['sachin',23,'m']]
df = pd.DataFrame(data)
print(df) 

data1=[['akash',40,'m'],['ak',40,'m']]
d1=pd.DataFrame(data1)
print(d1)

df=df.append(d1,ignore_index=True)
print(df)


###########################  continous numbers as 0 1 2 3 4 5
import pandas as pd
data=(['aaa','bbb','ccc','ddd'])
df=pd.DataFrame(data,index=[0,1,2,3])
print(df)

data1=(['eee','fff'])
df1=pd.DataFrame(data1,index=[4,5])
print(df1)

df=df.append(df1)
print(df)


















