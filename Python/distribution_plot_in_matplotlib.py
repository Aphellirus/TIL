#Import Module 
import numpy as np
import matplotlib.pyplot as plt

#create numpy array with 1000 values that follow normal dist with mean=10 and sd=2
data = np.random.normal(size=1000, loc=10, scale=2)

#Set x and y colors:
ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='red')

#create histogram
plt.hist(data, ec='black',color = 'green', bins=10)

#save and show
plt.savefig("plot.png")
plt.show()
