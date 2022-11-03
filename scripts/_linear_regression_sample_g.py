import matplotlib.pyplot as plt
import numpy as np

m = 20
theta1_true = 0.5
x = np.linspace(-1,1,m)
y = theta1_true * x

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16,8))
ax[0].scatter(x, y, marker='x', s=40, color='k')

def cost_func(theta1):

    theta1 = np.atleast_2d(np.asarray(theta1))
    return np.average((y-hypothesis(x, theta1))**2, axis=1)/2

def hypothesis(x, theta1):

    return theta1*x

theta1_grid = np.linspace(-0.2,1,50)
J_grid = cost_func(theta1_grid[:,np.newaxis])

ax[1].plot(theta1_grid, J_grid, 'k')


N = 5
alpha = 1
theta1 = [0]
J = [cost_func(theta1[0])[0]]
for j in range(N-1):
    last_theta1 = theta1[-1]
    this_theta1 = last_theta1 - alpha / m * np.sum(
                                    (hypothesis(x, last_theta1) - y) * x)
    theta1.append(this_theta1)
    J.append(cost_func(this_theta1))

colors = ['b', 'g', 'm', 'c', 'orange']
ax[0].plot(x, hypothesis(x, theta1[0]), color=colors[0], lw=2,label=r'$\theta_1 = {:.3f}$'.format(theta1[0]))

for j in range(1,N):
    ax[0].plot(x, hypothesis(x, theta1[j]), color=colors[j], lw=2, label=r'$\theta_1 = {:.3f}$'.format(theta1[j]))

# Labels, titles and a legend.
print(J)

ax[1].scatter(theta1, J, c=colors, s=40, lw=0)
ax[1].set_xlim(-0.2,1)
ax[1].set_xlabel(r'$\theta_1$')
ax[1].set_ylabel(r'$J(\theta_1)$')
ax[1].set_title('kainos funkcija')
ax[0].set_xlabel(r'$x$')
ax[0].set_ylabel(r'$y$')
ax[0].legend(loc='upper left')
plt.grid(True)
