# ''Secondstring''
# Ask user to input a sentance and return every second letter in reverse order
# Author: Conor McCaffrey

sentance = input('Please write a sentance') # asking user for sentance to carry out operation on
reversed_Sentence = sentance[::-1] # reversing the input
second_Letter = reversed_Sentence[::2] # taking every second letter from reversed sentence variable using W3 schools examples on slicing
print(second_Letter) # printing the resulting output
