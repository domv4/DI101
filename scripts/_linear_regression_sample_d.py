import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

plt.figure(figsize=(12,8))

data_set = load_boston()
x = data_set.data[:,5]
y = data_set.target

x = x[:10]
y = y[:10]

theta_0 = 10
theta_1 = 1

y_hat =  theta_0 + theta_1 * x

plt.plot(x, y_hat, '-y')
plt.scatter(x, y, s=80)

plt.xlabel("kambariai")
plt.ylabel("kaina tūkst.")
plt.grid(True)
