import matplotlib.pyplot as plt
import numpy as np
import random

x= np.arange(0.,6.28,0.5)
y1=np.sin(x)
y2=np.cos(x)

plt.figure(figsize=(100,5))

plt.plot(x,y1,"c",linewidth=5,linestyle="dashdot",marker="o",markeredgecolor="red",markersize=10)
plt.plot(x,y2,"co",linewidth=5,markeredgecolor="red",markersize=10)

plt.title("f(x)")
plt.xlabel("Input Values")
plt.ylabel("Trignometric Ratios")

plt.show()