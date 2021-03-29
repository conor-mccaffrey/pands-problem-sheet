# ''Squareroot''
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Conor McCaffrey


def sqrt(numtoCalc):  # defining the function and taking in one argument called 'numtoCalc'
    
    Guess = numtoCalc
    precision = 10 ** (-10)  # setting precision as per reference to assist in testing for closeness
    
    while abs(numtoCalc - Guess * Guess) > precision:  # while statement to check if our value is greater than the precision. If it is not, we stop looping
        Guess = (Guess + numtoCalc / Guess) / 2  # this is Newtons method. This will continue until we get a difference between approximations that is below our precision level
    
    print('The square root of', numtoCalc, 'is approx.' , round(Guess,1))  # Printing out the required output and rounding result to one decimal place

    return Guess # returning the value of Guess

sqrt(14.5)