# pands-problem-sheet

# Week 2 problem
Create a program that will intake attribute values and return an individual's Body Mass Index (BMI).

To do this, I will follow the workflow from this week's lectures using the Input function and Print function.
I will request the user to input their weight in kg, and their height in cm.
I originally thought of using the 'int' type but changed to 'float' to account for decimal places.
I will then convert these values (as inputs return 'string' format) to floats so I can use them to calculate thei BMI.
I will calcuate BMI based on the given formula (weight / height in metres squared) and return the user's BMI.
I then thank the user for using the program.

I started researching the layout of a BMI calculator from Stack Overflow (1)
For converting cm to m^2, I searched for the correct formula and used the formula on Python Programming (2).
General usage queries were resolved by consulting recommended testbook (3).

References : 
(1)Python, B., M, K. and Visser, S., 2021. BMI Calculator in Python. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/50386292#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.> [Accessed 28 January 2021].
(2)Arora, A., 2021. Calculate Body Mass Index (BMI) of an individual. [online] Python Programming. Available at: <https://www.pythonprogramming.in/calculate-body-mass-index-bmi-of-an-individual.html> [Accessed 28 January 2021].
(3)A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1

# Week 3 Problem
Create a program that asks a user to input a string and outputs every second letter in reverse order.

To complete this, I first thought about the process flow of the operation, as in which comes first : the reversing
operation or the 'taking ever second letter' operation. I played around with both ideas (incorporating W3 Schools (1)) and settled
on reversing the string first. To do this, I used the reverse function.

I set up the program by asking the user to input a sentence that would be the basis of the program, using the input functon.
I then reversed the string to allow downstream manipulations.
Using string slicing, I then took every second letter of the reversed sentence and finished off by printing the output onscree using
the print funtion. 

I made sure to add comments after each line to demonstrate how the function was behaving at each step, based upon directions given in 
the recommended textbook (2).

References:
(1)W3 Schools. 2021. Python - Slicing Strings. [ONLINE] Available at: https://www.w3schools.com/python/python_strings_slicing.asp. [Accessed 3 February 2021].
(2)A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1