import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,50)
y = np.linspace(-5,5,50)
X,Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X**2+Y**2))
plt.contour(X,Y,Z,levels=10,cmap='viridis')
plt.title("Contour Plot")
plt.colorbar()
plt.show()