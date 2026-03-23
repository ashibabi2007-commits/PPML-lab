import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [5,7,6,8,7]
plt.title("Scatter plot")
plt.plot(x,y,color='b',label="Scatter points")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()