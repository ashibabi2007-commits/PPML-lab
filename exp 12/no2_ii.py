import matplotlib.pyplot as plt
categories = ['A','B','C','D']
values = [3,7,8,5]
plt.bar(categories,values,color='g',label="Bar Data")
plt.title("Bar Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()