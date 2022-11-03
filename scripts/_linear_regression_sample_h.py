from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(figsize=(22,12),  subplot_kw={'projection': '3d'})
alpha = 1
r = np.linspace(-alpha,alpha,25)
X,Y= np.meshgrid(r,r)
l = 1./(1+np.exp(-(X**2+Y**2)))
ax.plot_surface(X, Y, l, cmap = 'rainbow')
ax.set_xlabel('θ 0')
ax.set_ylabel('θ 1')
ax.set_zlabel('J(θ 0,θ 1)')
ax.view_init(45, 45)
plt.show();