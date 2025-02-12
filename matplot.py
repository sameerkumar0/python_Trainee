import matplotlib.pyplot as plt

import numpy as np
x=np.linspace(1,10,100)
y=np.sin(x)
plt.plot(x,y,label="sine wave",linestyle="--",color="blue",linewidth=2)
plt.title("Simple plot ")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()