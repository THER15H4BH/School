import pandas as pd
import numpy as mp

o1=pd.DataFrame(mp.random.rand(5,4))
print(o1,type(o1),sep="\n")
print()

o2=pd.DataFrame([[1,2,3],[2,3],[3,4]],dtype=mp.float64)
print(o2)
print()

dict1={
    "Sherlock":3,
    "Holmes":4
}
o3=pd.DataFrame(dict1,index=["I"])
print(o3)
print()

dict2={
    'Golem': {'name': 'John', 'age': mp.NaN,'class':'4'},
    'Pekka': {'name': 'Marie', 'age': '22', 'sex': 'Female'}
}
o4=pd.DataFrame(dict2)
print(o4)
print()
#print(o4.columns,o4.index,o4.axes,o4.dtypes,o4.size,o4.shape,o4.empty,o4.ndim,len(o4),sep="\n")
#print(o4.count())
#print(o4.count(1))
#print(o4.T)
#print(o4.Golem)
print(o4.Golem["age"],type(o4.Golem))
print()
print(o1)
print(o1[0][0])
print(o1.loc[0,0])
print(o1.at[0,0])

print()
print()

#print(o1.loc[2:3,:])
#print(o1.loc[:,1:3])
print(o1.iloc[2:3,1:3])

o1.at[:,4]=55
print(o1)
o1=o1.assign(Pok=89)
print(o1)

print()
o1.loc[5,:]=15
o1.at[6,:]=20
print(o1)

o1[0][0]=0.9
o1.iloc[0,1]=0.8
o1.iat[0,2]=0.7
print(o1)

del o1[4]
print(o1)
o1=o1.drop([6,5],axis=0)
o1=o1.drop(["Pok"],axis=1)
print(o1)

o1.rename(index={0:"A",1:"B",2:"C",3:"D",4:"E"},columns={0:"IRAQ",1:"RUSSIA",2:"MEXICO",3:"CHAD"},inplace=True)
print(o1)
print(o1["IRAQ"]["A"])
print(o1.IRAQ["A"])
print(o1.iloc[0,0])
print(o1.iat[0,0])
print(o1.loc["A","IRAQ"])
print(o1.at["A","IRAQ"])

o1.rename(index={"C":"A"},inplace=True)
print(o1)
print(o1.loc["A"])
print(o1.loc["A",:])