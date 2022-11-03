import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plot_regression_line(x, y):
    plt.figure(figsize=(12,6))
    plt.style.use('seaborn')
    plt.scatter(x, y, color = "m", marker='x', s = 30)
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()
  
def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    plot_regression_line(x, y)
  
main()