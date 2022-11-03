import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
plt.style.use('fivethirtyeight')
m = 1
b = 1

def function(x):
    return 2*x**2
  
def deriv(x):
    return derivative(function, x)
  
def calculate_secant(x, y):
    points = [2, 8]
    m, b = np.polyfit(x[points], y[points], 1)
    return m * x + b    

y = np.linspace(-2.5, 5) 

Yp = y[-10]
xp         = [0,2]
yp = [function(x) for x in xp]
plt.figure(figsize=(10,6))
plt.plot(y, function(y), color='black', lw=3 ,label='f(x)=2x²')
plt.scatter(xp, yp, s=100, c='r')
plt.plot(y, deriv(y), color='green', label='Išvestinė')
plt.legend(loc='upper left')
plt.grid(True)