import numpy as np
import matplotlib.pyplot as plt
'''

listofNumbers = [1,2,3,9,7]
numbers = np.array([1,5,8])

#listofNumbers = listofNumbers + 3
numbers = numbers * np.array([1,4,6])

print(numbers)
print(listofNumbers)

randomNumbers = np.random.randint(100,200,5)
print(randomNumbers)
'''

#xpoints= np.array(range(1,101))
#ypoints = xpoints * xpoints


xpoints = np.array([1,2,4,7]) # this is for plotting multiple points. Add 'o' to plot function to remove the line
ypoints = np.array([4,8,9,6]) # add marker ='o' for highlighted points

# add linestyle = 'dotted' to plot function (or dashed)  linestyle can be written as ls. 
# dotted can be written as :. dashed can be written as --. Can change color too using color = 'r' or c instead of colour
#You can plot as many lines as you like by simply adding more plt.plot() functions:
'''
** setting fonts for things **
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

'''
#plt.plot(xpoints,ypoints, label= 'xSquared')   # first arg is for x-axis, second arg is for y-axis
#plt.plot(xpoints,xpoints, label='straight', color='blue')  # x points on both arguments make sit straight


plt.plot(xpoints,ypoints, marker = 'o', linestyle = 'dashed')
plt.grid(linewidth = 1.5) # writing axis = 'x'(or 'y') determines which to show. Can also set other properties like ls or linewidth = 0.5 
plt.title('This is the title')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#plt.legend()
#plt.show()

#randompoints = np.random.randint(1,1000, 100)
#plt.scatter(xpoints,randompoints, label= 'Random')


plt.show()


