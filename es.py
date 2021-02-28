# ' Counting e's '
# Write a program that reads in a text file and outputs the number of e's it contains.
# Author : Conor McCaffrey

import os   # import the os module

def readLetter(file):   # define our function
    list1 = []   # this is an empty list. We will store occurences of 'e' in here
    if (os.path.exists(file)):  # check first that the file you are inputting exists
            with open(file, 'rt') as f:  # open the file in read mode and assign it as 'f'
                data = f.read() # read the contents of the file and assign to variable 'data'
                for char in data: # for loop. For each character in our datafile
                    if char.lower() == 'e': # if the letter is e (I have added lower function to account for capital 'E' also)
                        list1.append(char) # add the occurence of the letter 'e' to my list which is defined at start of the function
                print(len(list1))    # print the length of the list therefore, the occurences of the letter 'e'
    else: # I added this to account for errors in inputting file name
        print('FileNotFound') 

readLetter('georgeOrwell.txt')