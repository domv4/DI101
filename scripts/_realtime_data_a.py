import random
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    
    # clear the current axes
    plt.cla()
    
    plt.plot(x_vals, y_vals)
    
ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.tight_layout()
plt.show()