posInt = int(input('Please enter a positive integer'))

print (posInt)
while posInt != 1:
    if posInt % 2 == 0 :
        posInt = (posInt // 2)
        print (posInt)
    elif posInt % 2 != 0:
        posInt = ((posInt * 3) + 1)
        print(posInt)

