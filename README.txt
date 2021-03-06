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
the print funtion. I consulted other examples upon completion of the code (2).

I made sure to add comments after each line to demonstrate how the function was behaving at each step, based upon directions given in 
the recommended textbook (3).

References:
(1)W3 Schools. 2021. Python - Slicing Strings. [ONLINE] Available at: https://www.w3schools.com/python/python_strings_slicing.asp. [Accessed 3 February 2021].
(2) Docs.python.org. 2020. 7.1. String — Common String Operations — Python 2.7.17 Documentation. [online] Available at: https://docs.python.org/2/library/string.html [Accessed 4 February 2021].
(3)A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1

# Week 4 Problem
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

This task was a 'step up' on previous tasks. This involved some logic thinking in addition to coding abilities learned 
from the lecture slides.

To complete this, I played around with different loops gaining some familiarity with how they worked, while consulting the recmommended
reading material (1,2).

I then thought about the logic and flow of the loop. I broke down the problem to several individual segments. One segement was the test to determine
if the integer was even and how to respond (divide result by two, using floor division to ensure an integer is returned and not a float).
The next segment was how to respond if number was odd (multiplying by 3 and adding 1, using brackets to control the order of operations) and the final
segement was to break the flow if the value was 1. To carry this segment, I encompassed my 'if' loop in a 'while' statement. Using a 'while' loop
ensured the loop would indeed 'loop around', unlike an 'if' control flow statement. I also consulted another example to make sure the process flow of 
my code was similar to other examples (3). 

References:
 (1)A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1
 (2) Automatetheboringstuff.com. 2020. Automate The Boring Stuff With Python. [online] Available at: https://automatetheboringstuff.com/chapter3/ [Accessed 9 February 2021].
 (3) Stack Overflow. (n.d.). Collatz Sequence. (Python 3). [online] Available at: https://stackoverflow.com/questions/33324432/collatz-sequence-python-3 [Accessed 10 February 2021].


# Week5 Problem
Write a program that outputs whether or not today is a weekday.

Again, this weeks task was another 'step-up' in difficulty level. I first consulted the recommended textbook for general examples regarding the use of lists,
sets and dictionaries. Quite quickly, it became clear using lists was the best way to complete the task.

I made two lists: one for weekdays and one for the days of the weekend. The list containing days of the weekend was probably not overly
necessary for my solution, but I wanted to include it just for completeness. 

I consulted w3schools (2) for the use of the datetime module and how to import it. I combined this with the 'format' attribute detailed in previous lectures
to get the current day in ' full-string format (%A)'.

I then constructed a simple 'if' statement that would search our constructed lists with the current day. If the current day appeared in either list (which it almost surely should!)
then a pre-determined response would be the output.

The next step to this program would be to wrap it in a function to allow the user to simply call the function without needing to construct the 'if' statement everytime.

References:
(1) A Whirlwind Tour of Python by Jake VanderPlas (O’Reilly). Copyright 2016 O’Reilly Media, Inc., 978-1-491-96465-1
(2) w3schools. 2021. Python Dates. [ONLINE] Available at: https://www.w3schools.com/python/python_datetime.asp. [Accessed 18 February 2021].


# Week 6 Problem

To begin this problem, I looked into what Newtons Method actually was and how it could be applied in finding the approximate square root of a number. To to this, I consulted several
sites suchs as StackExchange (1) , GeekforGeeks (2) , Medium (3) and School for Champions(4). I came across several examples of how to carry out the required task and looked into how I
would adapt the examples
to align with our needs. 

I defined the function and asked the user to input a positive number which I then converted to a float.

I then iniatied another variable I called 'Guess' (leaning heavily on the School for Champions (4) text).

I knew immediately a 'for' loop would be required so I also included a default argument in our defined function for clarity. I set the 'number of iterations' to 10 mostly to ensure the correct result would be attained (setting 
the number of iterations to 1 gave a result of 4.6). The variable 'Guess' was set to the formula of Newton's method outline in refereces 1-4 (( x_(n+1) = 0.5 * (x_n +a / x_n))). I added a 'print'
function at the end, incorporating our variables, in order to align the function with the example given. This is also why I added the round function to ensure one decimal place. I looked over my example and determined if it function
sililarly to the idea of Newton's Method (5).

References:
(1) https://math.stackexchange.com/questions/3524205/square-roots-by-newton-s-method
(2) GeeksforGeeks. 2021. Find root of a number using Newton's method - GeeksforGeeks. [ONLINE] Available at: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/. [Accessed 24 February 2021].
(3) https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
(4) Newton's Square Root Approximation by Ron Kurtus - Succeed in Understanding Algebra: School for Champions. 2021. Newton's Square Root Approximation by Ron Kurtus - 
    Succeed in Understanding Algebra: School for Champions. [ONLINE] Available at: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YDb0jWj7TIW. [Accessed 25 February 2021].
(5) En.wikipedia.org. 2020. Newton's Method. [online] Available at: https://en.wikipedia.org/wiki/Newton%27s_method [Accessed 25 February 2021].    

# Week 7 Problem

For this week's problem, I brought in a little bit of my prior experience of Python (MTA certification). I researched several websites to gain an idea of the process flow for counting characters, looking at sites such as 'Geek for Geeks' (1)
and Python Examples (2). I also gained further exposure the file handing using W3School (3). I first constructed a text file based on the first few pages of
George Orwell's 1984 book. I imported the os module as per the tutorials.

I defined our function, which accepted one input (the file). I then created an empty list (list1) which would be used to hold each occurence of the letter 'e' in our text file. I also included a line to ensure 
that the inputted file actually exists. If the file does exist, I requested the function to open it in 'read' mode, assigning the action to the variable 'f'. I then read the file and assigned the action to the variable 'data'. 
I iniatied a 'for' loop to access each letter in our file and set it each occurence of the letter 'e' (drawing on the examples given in Stack Overflow (5)). I also used the lower() attribute to account for capital 'E'. For each occurence of the letter 'e', the result is stored in my newly formed
list (list1). I then asked the function to print the length of the newly formed list, therefore counting the occurences of the letter 'e'. 

I set up the majority of the function inside an 'if' statement, with the 'else' componant accounting for if the file does not exist and also to account for spelling errors when entering the filename.
I have included the text file I used for reference but not sure if this is correct.

References:
(1) GeekforGeeks. 2021. Count the number of times a letter appears in a text file in Python. [ONLINE] Available at: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/. [Accessed 28 February 2021]
(2) PythonExamples. 2021. Python – Count Number of Characters in Text File. [ONLINE] Available at: https://pythonexamples.org/python-count-number-of-characters-in-text-file/#1. [Accessed 28 February 2021].
(3) PythonFileOpen. 2021. Python File Open. [ONLINE] Available at: https://www.w3schools.com/python/python_file_handling.asp. [Accessed 28 February 2021]
(5) Python, C., Pieters, M. and Smith, A., 2020. Counting Specific Letters Or Symbols In A Text File In Python. [online] Stack Overflow. 
    Available at: https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python [Accessed 28 February 2021].
