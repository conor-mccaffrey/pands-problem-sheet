# *Python Collatz* Create a program that asks the user to input any positive integer and
# outputs the successive values of the following calculation
# Author : Conor McCaffrey

posInt = int(input('Please enter a positive integer'))

print (posInt)
while posInt != 1:
    if posInt % 2 == 0 :
        posInt = (posInt // 2)
        print (posInt)
    elif posInt % 2 != 0:
        posInt = ((posInt * 3) + 1)
        print(posInt)

