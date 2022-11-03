import matplotlib.pyplot as plt
import numpy as np

theta1 = 2

x = np.array([1,2,3])
y = np.array([1,2,3])
m = len(x)

def cost_func(theta):
    error = 0
    for i in range(m):
        error += ((theta*x[i])-y[i])**2
    return error/(2*m)

def hypothesis(x, theta):
    return x * theta


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,5))
ax[0].plot(x, hypothesis(x,theta1), marker='x',color='k')
ax[0].scatter(x, y, marker='x', s=80, c='red')

print('J(θ1): ',cost_func(theta1))
ax[1].scatter(theta1, cost_func(theta1), marker='x', s=150, c='b')     
ax[1].set_title('kaina')
ax[0].set_title('hipotezė')
ax[1].set_xlim(-0.5,3)

print(np.round(cost_func(theta1),2))
plt.show()