import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,8,6,10]

plt.scatter(x,y,label='Scatter 1',color='r')
plt.scatter(y,x,label='Scatter 2',color='b')

plt.title("Interesting Info")
plt.ylabel("population")
plt.xlabel("ages")


plt.legend()
plt.show()