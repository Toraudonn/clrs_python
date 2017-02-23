from matplotlib import pyplot as plt
import numpy as np
import scipy as sci


pts = np.array([(1,1), (2,4), (3,1), (9,3), (12, 9)])

x = pts[:,0]
y = pts[:,1]

z = np.polyfit(x, y, 3)
f = np.poly1d(z)

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x, y, 'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1]+1])
plt.show()