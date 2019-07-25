import matplotlib.lines as mlines
import matplotlib.pyplot as plt
# defining legend style and data
blue_line = mlines.Line2D([], [], color='blue', label='My Label')
reds_line = mlines.Line2D([], [], color='red', label='My Othes')

plt.legend(handles=[blue_line, reds_line])

plt.show()