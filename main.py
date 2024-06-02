import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import yfinance as yf

# Download historical data for Apple Inc.
apple = yf.download("NVDA", start="2015-12-01", end="2024-05-10")


histdf = pd.DataFrame(apple)


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2,color = 'Black')
ax.set_title('Nvidia Corp. Stock Price')
ax.set_xlabel('Date')
ax.set_ylabel('Close Price')
ax.grid()

def init():
    ax.set_xlim(histdf.index.min(), histdf.index.max())
    ax.set_ylim(histdf['Close'].min(), histdf['Close'].max())
    line.set_data([], [])
    return line,


def update(frame):
    x = histdf.index[:frame]
    y = histdf['Close'][:frame]
    line.set_data(x, y)
    return line,


ani = FuncAnimation(fig, update, frames=len(histdf), init_func=init, blit=True,interval = 5)


plt.show()
