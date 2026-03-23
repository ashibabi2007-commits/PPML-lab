import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,25,30]
plt.plot(x,y)
plt.title("Sample Line Plot")
plt.plot(x,y,linestyle='--', color='r', marker='o', label="Data Line")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()