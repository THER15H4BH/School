import pandas as pd

dict1={
    "Sherlock":[1,2,3],
    "Holmes":[4,5,6]
}

dfobj1=pd.DataFrame(dict1)
print(dfobj1)
#print(dfobj1["Sherlock"])

#dfobj1["Sherlock"][1]=10
#print(dfobj1)

#dfobj1.to_csv("First1.csv")
#dfobj1.to_csv("First2.csv",index=False)

#print(dfobj1.head(2))
#print(dfobj1.tail(1))

#print(dfobj1.describe())

dfobj2=pd.read_csv("First3.csv")
print(dfobj2.head(3))

dfobj1.index=["First","Second","Third"]
print(dfobj1)