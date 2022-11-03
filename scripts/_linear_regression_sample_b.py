import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_regression_line(x, y, b):
    plt.figure(figsize=(12,6))
    plt.style.use('seaborn')
    plt.scatter(x, y, color = "m", marker='x', s = 30)
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
  
def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    model = LinearRegression()
    model.fit(x, y)
    b = model.coef_[0], model.intercept_
    plot_regression_line(x, y, b)
  
main()