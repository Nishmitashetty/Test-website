#adding a legend
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x, x*1.5, label = 'Normal')
plt.plot(x, x*3, label = 'Fast')
plt.plot(x, x/3, label = 'Slow')
plt.legend()
plt.show()
