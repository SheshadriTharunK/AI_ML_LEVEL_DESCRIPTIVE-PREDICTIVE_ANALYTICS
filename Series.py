import pandas as pd 
titanic=pd.read_csv("C:\\Users\\Tharun\\Downloads\\titanic\\train.csv")
print(titanic)
print(type(titanic)) 
titanic.shape
print(titanic['Survived'].to_string(index=False))
print(titanic.Pclass.to_string(index=False))


#series -- an array with custom index 

import pandas as pd
s1=pd.Series([10,20,30,40])
print(type(s1))
print(s1.head())
print(s1.shape)
print(s1.index)

<class 'pandas.core.series.Series'>
0    10
1    20
2    30
3    40

dtype: int64
(4,)
RangeIndex(start=0, stop=4, step=1)

print(s1[0]) 
print(s1[0:3])
print(s1[[1,3]]) #fancy indexing -- in the indexs we will give the indexes as list -- which we want  

10
0    10
1    20
2    30
dtype: int64
1    20
3    40
dtype: int64
print(s1[s1>30]]) # 3 40 


1    10
3    20
5    30
7    40
dtype: int64


-- accessing and indexing 
s2=pd.Series([10,20,30,40],index=[1,3,5,7])
print(s2[1]) #indexing refers  explicit index 
print(s2[1:5]) # slicing refers to implicit index
print(s2[0:3]) ## slicing refers to implicit index

s2=pd.Series([10,20,30,40],index=[1,3,5,7])
print(s2.iloc[1])
print(s2.iloc[1:3])
print(s2.iloc[[1,3]])
print(s2.iloc[s2>35]) # iloc doesn't allows mask based indexing 

#iloc -- implicit indexing 

s2=pd.Series([10,20,30,40],index=[1,3,5,7])
print(s2.loc[1]) 
print(s2.loc[1:3])
print(s2.loc[[1,3]])
print(s2.loc[s2>35])

#aggregates 

print(s2.mean())
print(s2.max())
print(s2.min())
print(s2.sum())

























