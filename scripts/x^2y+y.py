from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def bilinear1(x,y):
    return x**2*y+y

fig = plt.figure(figsize=(10,8))
ax = plt.axes(projection='3d')

x = np.linspace(0, 10)
y = np.linspace(0, 10)
X, Y = np.meshgrid(x,y)

Z = bilinear1(X,Y)

ax.set_xlabel('x', fontsize=14) 
ax.set_ylabel('y', fontsize=14) 
ax.set_zlabel('f(x,y)', fontsize=14)

ax.plot_surface(X,Y,Z, rstride=2, cstride=2);