import random
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

index = count()

def animate(i):
    data = pd.read_csv('../data_samples/test_data.csv')
    
    x_   = data['x_value']
    y1   = data['total_1']
    y2   = data['total_2']
    
    # clear the current axes
    plt.cla()
    
    plt.plot(x_, y1, label='channel 1')
    plt.plot(x_, y2, label='channel 2')
    
    plt.legend(loc='upper left')
    plt.tight_layout()
    
ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.show()