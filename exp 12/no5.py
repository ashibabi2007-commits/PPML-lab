import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x = [1,2,3,4,5]
y = [5,6,7,8,9]
z = [2,3,3,3,2]
ax.scatter(x,y,z,color='r',label='3D points')
ax.set_title("3D scatter plot")
ax.set_xlabel('X-Axis')
ax.set_ylabel("Y-Axis")
ax.set_zlabel("Z-Axis")
plt.legend()
plt.show()