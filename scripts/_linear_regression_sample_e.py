import numpy as np
import matplotlib.pyplot as plt

theta0 = 0
theta1 = 1
def model(x):
    return theta0 + x * theta1 

def plot_regression_line(x, y):
    plt.figure(figsize=(12,6))
    plt.scatter(x, y, color = "y", s = 80)
    plt.plot(x, model(x))
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()
  
def main():
    x = np.array([1, 2, 3]).reshape(-1, 1)
    y = np.array([1, 2, 3])
    plot_regression_line(x, y)
  
main()