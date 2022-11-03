import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

m = 1
b = 1

def function(x):
    return m*x + b
  
def deriv(x):
    return derivative(function, x)
  
y = np.linspace(0, 10) 

Yp = y[-10]
# plt.plot(Xp, Yp, marker='o')
# plt.vlines(Xp, min(Y), Yp, linestyles='dashed')
# plt.hlines(Yp, min(X), Xp, linestyles='dashed')
xp         = [2,8]
yp = [function(x) for x in xp]
plt.figure(figsize=(10,8))
#plt.plot(y, function(y), '-gX', markevery=markers_on, color='black', lw=3 ,label='f(x)=2x')
plt.plot(y, function(y), color='black', lw=3 ,label='f(x)=mx + b')
plt.scatter(xp, yp, s=100, c='r')
plt.plot(y, deriv(y), color='green', label='Išvestinė')
plt.legend(loc='upper left')
plt.grid(True)