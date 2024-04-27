from collections import deque
from itertools import count
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

xLable = deque(maxlen=30)
data1 = deque(maxlen=30)

data2 = data1

data3 = data1

index = count()

def animate(i):
    xLable.append(next(index))
    print(xLable)
    data1.append(random.randrange(0, 9)*0.1 + 220)
    plt.cla()
    plt.plot(xLable, data1)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=500)


ax = plt.axes()
ax.set_facecolor("#00416A")

plt.ylabel('Voltage')
#hide x and y axis lable
#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)
plt.show()