import matplotlib.pyplot as plt

ages = [20,21,23,43,54,43,5,34,23,12,43,45,6,4,23,4,13]
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins,histtype='bar',rwidth=0.8)

plt.title("Interesting Info")
plt.ylabel("population")
plt.xlabel("ages")


plt.legend()
plt.show()
