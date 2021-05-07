import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x, x*1.5, label = 'Normal')
plt.plot(x, x*3, label = 'Fast')
plt.plot(x, x/3, label = 'Slow')
plt.grid(True)
plt.title('Sample Growth of a Measure')
plt.xlabel('Sample')
plt.ylabel('Values Measured')
plt.legend(loc = 'upper right')
plt.savefig(R'C:\Users\10645863\Desktop\Python Programs\plot123.png')
plt.show()
