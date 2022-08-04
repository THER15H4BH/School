import matplotlib.pyplot as plt
import numpy as np
import random

Medals=["Gold","Silver","Bronze"]

MedalsOfCountries=[[5,25,45],[4,23,49],[6,22,47]]

X=np.arange(len(Medals))

plt.bar(Medals,MedalsOfCountries[0],width=0.25,color="red")
plt.bar(X+.25, MedalsOfCountries[1],width=0.25,color="g")
plt.bar(X+.5, MedalsOfCountries[2],width=0.25,color="c")

plt.show()