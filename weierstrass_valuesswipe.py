import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

M = 10000 #precision
blim = 3 #max b value
fm = 10 #frame multiplier
w = 5 #wait frames
ad = 8 #a values changes

x = np.linspace(-2,2,M)

fig, ax = plt.subplots()
ax.set_xlim(-2,2) 
ax.set_ylim(-2,2)
a_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
b_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)
line, = ax.plot(0,0)

def weierstrass(x, N ,a ,b):
	y = np.zeros((1,M))
	for n in range(1,N):
		y = y + np.cos(b**n*np.pi*x)/a**n
	return y

def animation_frame(i):
    bl = blim * fm
    if i <= bl: 
        av = 2
        bv = i/fm
    elif i > bl and i <= bl + w:
        av = 2
        bv = blim
    elif i > bl + w and i <= bl + ad + w:
        av = 2 + ( (i-w)/fm - blim)
        bv = blim
    else:
        av = 9
        bv = blim
    y = np.reshape(weierstrass(x,500, av ,bv),(M,))
    a_text.set_text('1/a = %.1f' % av)
    b_text.set_text('b = %.3f' % bv)
    line.set_xdata(x)
    line.set_ydata(y)
    return line, a_text, b_text

animation = FuncAnimation(fig, func = animation_frame, frames = np.arange(1, blim  * fm + ad + 2 * w, 1), interval = 10, blit = True)
#animation.save('weierstrass_valuesswipe.gif', fps = 24, dpi = 80)
plt.show()