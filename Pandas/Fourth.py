import pandas as pd
import numpy as mp

dict={"ame":["Ram","Sam","Mam"],"arks":["70,95,80"]}

df=pd.DataFrame(dict,index=[1,2,3])

for i,j in df.iteritems():
    if i=="arks":
        print(j)