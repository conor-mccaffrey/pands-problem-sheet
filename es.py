# ' Counting e's '
# Write a program that reads in a text file and outputs the number of e's it contains.
# Author : Conor McCaffrey

import os   # import the os module

filetoImport = str(input("Please enter the name of the file you would like to import: "))   # the user is prompted to enter name of txt file as string
if (os.path.exists(filetoImport)):  # check first that the file you are inputting exists

    with open (filetoImport, 'r') as text_file: # opens text file you have entered in read mode and assigned the variable text_file
        data = text_file.read()      # read the contents of the file and assign to variable 'data' 
        lower_e = data.count('e') # lower_e is equal the number of occurences of lower-case 'e'
        higher_E = data.count('E') # higher_E is equal the number of occurences of higher-case 'E'
        print(lower_e + higher_E)   # prints the total amount of lower case 'e' and high case 'E'