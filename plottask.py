# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.
# Author : Conor McCaffrey

import numpy as np, matplotlib.pyplot as plt   # importing libraries and assiging aliases

x = np.arange(0.0,4.0,1.0)   # setting the range as described in task and in RealPython reference

y1 = x   # plotting the points on y-axis
y2 = x**2 #plotting the points on y-axis
y3 = x**3 #plotting the points on y-axis

font = {'family': 'serif', 'color':'darkred','weight': 'normal', 'size':20} # adding in fonts
font1 = {'family':'serif','color':'navy','size':10}   # adding in fonts

plt.plot(y1, color='#575daa', ls='-.', lw = 2, 
         marker='s', ms = '5', mec='black', mfc='hotpink', label='f(x)=x')  # plotting each point and making the plot pretty
plt.plot(y2, color='#57de5a', ls='-.', lw = 2, 
         marker='o', ms ='5', mec='black', mfc = 'hotpink', label='g(x)=x^2')  # plotting each point and making the plot pretty
plt.plot(y3, color='#ff0202', ls='-.', lw = 2, 
         marker='o', ms ='5', mec='black', mfc = 'hotpink', label='h(x)=x^3')  # plotting each point and making the plot pretty

plt.xlabel('x-axis', fontdict=font1)  # adding labels
plt.ylabel('y-axis', fontdict=font1)   # adding labels
plt.title('Plot Task', fontdict=font, loc = 'left')  # adding a title and properties
plt.legend()   # adding a legend for clarity
plt.grid(axis = 'y', color = 'green' , lw = 0.1) # adding a y=axis grid and setting properties
plt.show()   # displaying the graph
# plt.savefig('plottask.png')   # adding code here that would be used to save the file if we did not want to show it 