import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,6,8,9,5]
eating =   [2,3,1,4,2]
working =  [7,8,9,5,6]
playing =  [8,7,6,6,11]

plt.plot([],[],color='m',label='Sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.title("Interesting Info")
plt.ylabel("population")
plt.xlabel("ages")


plt.legend()
plt.show()