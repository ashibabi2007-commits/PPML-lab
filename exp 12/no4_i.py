import matplotlib.pyplot as plt
sizes = [15,30,45,10]
labels = ['A','B','C','D']
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
explode = (0,0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("Pie Chart")
plt.axis('equal')
plt.show()