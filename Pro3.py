#How to add style to graph
import matplotlib.lines as mlines
from matplotlib import pyplot as plt
from matplotlib import style

#style.use("fivethirtyeight")
style.use("ggplot")

x = [1,3.8,4,5,4.9]
y = [10,20,30,40,50]

x2 = [1,1.2,3.40,5,4]
y2 = [10,20,30,40,50]

plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'r',label='line two',linewidth=5)
plt.title("Interesting Info")
plt.xlabel("x axis")
plt.ylabel("y axis")

# blue_line = mlines.Line2D([], [], color='blue', label='My Label')
# reds_line = mlines.Line2D([], [], color='red', label='My Othes')
#
# plt.legend(handles=[blue_line, reds_line])

plt.legend()

plt.grid(True,color='b')
plt.show()



'''
The ones with distinctive looks are:

seaborn-*
This is a set of styles from the Seaborn project [2]. The project is a complement to Matplotlib, providing additional features and improving the default matplotlib aesthetics. Ones I particularly like are seaborn-deep, seaborn-pastel and seaborn-white.

dark_background
The dark_background style is the standard matplotlib one (e.g. classic) with colours changed for high contrast.

Example charts using the Matplotlib seaborn-white style
bmh
This style comes from Bayesian Methods for Hackers [3] book. I find it particularly suits scientific graphing by showing the precision of the plot.

ggplot
This style comes from the plotting system of the same name for the R language [4]: it takes on a lot of contemporary lessons on presenting data, focusing on simplicity.

fivethirtyeight
This style emulates the look and feel of the famous data journalist Nate Silver's site fivethirtyeight.com.
'''

