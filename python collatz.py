# *Python Collatz* Create a program that asks the user to input any positive integer and
# outputs the successive values of the following calculation
# Author : Conor McCaffrey

posInt = int(input('Please enter a positive integer')) #ask user for a positive integer

print (posInt) #print off the input integer
while posInt != 1: #easy way to end the loop if the current value is 1
    if posInt % 2 == 0 : # test to see if input is even
        posInt = (posInt // 2) # this will execute if integer is even, floor division of the integer
        print (posInt) # print off the current value of the input
    elif posInt % 2 != 0: # elif statement accounts for if input is odd, testing inequality
        posInt = ((posInt * 3) + 1) # this will execute of input is odd
        print(posInt) # print value of 'odd' integer
