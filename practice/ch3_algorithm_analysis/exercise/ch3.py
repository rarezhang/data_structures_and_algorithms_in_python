__author__ = 'wlz'


import matplotlib.pyplot as plt
import math

# R-3.1
x = range(1,100)
y1 = [8*i for i in x]   # 8n
y2 = [4*i*math.log(i,2) for i in x]   # 4nlogn, base is 2
y3 = [2*i**2 for i in x]   # 2n**2, log base is 2
y4 = [i**3 for i in x]   # n**3
y5 = [2**i for i in x]   # 2**i
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.xscale('log')  # using a logarithmic scale for the x-axes
plt.yscale('log')  # using a logarithmic scale for the y-axes
plt.legend(['y = 8x', 'y = 4xlogx', 'y = 2x^2', 'y = x^3', 'y = 2^i'], loc='upper left')  # add legend for the picture
plt.show()