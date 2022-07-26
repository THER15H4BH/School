import pandas as pd
import numpy as mp

srobj1=pd.Series(mp.random.rand(5),range(1,6,1))
#print(srobj1)

srobj2=pd.Series(mp.arange(45,100,4.5))
#print(srobj2.head())

srobj3=pd.Series(mp.tile([4,5],4))
#print(srobj3)

srobj4=pd.Series(mp.linspace(40,90,7))
#print(srobj4)
#print(srobj4.describe())

print(srobj1)
srobj1[1]=15
print(srobj1)

print(srobj1.index)
print()

srobj5=pd.Series({"Ja":31,"Fe":mp.NaN,"Ma":31})
print(srobj5)
print(srobj5.index)
print(srobj5.values)
print(srobj5.dtype)
print(srobj5.size)
print(srobj5.empty)
print(srobj5.ndim)
print(srobj5.nbytes)
print(srobj5.hasnans)
print(srobj5.shape)
print(srobj5.values.itemsize)
print()

srobj6=pd.Series(5,index=range(5),dtype=mp.float64)
print(srobj6)
srobj6=srobj6[::-1]
print(srobj6)
srobj6.index=[4,5,6,7,8]
print(srobj6[4])
srobj6[0:3]=10
print(srobj6)

#srobj7=pd.Series(srobj1)
#print(srobj7)