import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[10,20,30,40,50],label="Demo 1")
plt.bar([2,4,6,8,10],[20,30,50,60,10],label="Demo 2")

plt.title("Interesting Info")
plt.xlabel("x axis")
plt.ylabel("y axis")


plt.legend()
plt.show()
