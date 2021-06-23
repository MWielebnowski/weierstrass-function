import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

b = 2 #best results for int b > 1
fm = 20 #frame multiplier

if b % 2 == 0:
    M = 10000 #override for greater precision
    mm = 1.6
    dy = 2 * b
else:
    M = 100000 #higher values cause severe pefrormance penalty 
    mm = 1.8
    dy = 1

x = np.linspace(-2,2,M)
fig, ax = plt.subplots()
ax.set_xlim(-2,2) 
ax.set_ylim(-2,2)
line, = ax.plot(0,0)

def weierstrass(x, N ,a ,b):
	y = np.zeros((1,M))
	for n in range(1,N):
		y = y + np.cos(b**n*np.pi*x)/a**n
	return y

def animation_frame(i): 
    y = np.reshape(weierstrass(x,500,2,b),(M,))
    if i <= fm:
        ax.set_xlim(-2 + mm*i/(1*fm) + i/(b*fm),2 - mm*i/(1*fm) + i/(b*fm))
        ax.set_ylim(-2 + mm*i/(1*fm) - i/(dy*fm),2 - mm*i/(1*fm) - i/(dy*fm))
    else:
        j = fm - (i - fm)
        ax.set_xlim(-2 + mm*j/(1*fm) + j/(b*fm),2 - mm*j/(1*fm) + j/(b*fm))
        ax.set_ylim(-2 + mm*j/(1*fm) - j/(dy*fm),2 - mm*j/(1*fm) - j/(dy*fm))
    line.set_xdata(x)
    line.set_ydata(y)
    return line,

animation = FuncAnimation(fig, func = animation_frame, frames = np.arange(1, 2 * fm , 1), save_count = 2 * fm)
#animation.save('weierstrass_fractalzoom.gif', fps = 24, dpi = 80)
plt.show()