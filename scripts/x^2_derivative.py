import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

m = 1
b = 1

def function(x):
    return x**2
  
def deriv(x):
    return derivative(function, x)
  
def calculate_secant(x, y):
    points = [2, 8]
    m, b = np.polyfit(x[points], y[points], 1)
    return m * x + b    

y = np.linspace(-2.5, 5) 

Yp = y[-10]
# plt.plot(Xp, Yp, marker='o')
# plt.vlines(Xp, min(Y), Yp, linestyles='dashed')
# plt.hlines(Yp, min(X), Xp, linestyles='dashed')
xp         = [0,2]
yp = [function(x) for x in xp]
plt.figure(figsize=(10,8))
#plt.plot(y, function(y), '-gX', markevery=markers_on, color='black', lw=3 ,label='f(x)=2x')
plt.plot(y, function(y), color='black', lw=3 ,label='f(x)=x²')
#plt.plot(y, calculate_secant(y, function(y)))
plt.scatter(xp, yp, s=100, c='r')
plt.plot(y, deriv(y), color='green', label='Išvestinė')
plt.legend(loc='upper left')
plt.grid(True)