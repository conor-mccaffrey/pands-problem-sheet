# ''Squareroot''
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Conor McCaffrey

def sqrt(numOfIterations=10):    # I have set this to 10 arbitrarily in oredr to ensure enough loops occue to capture the closest value
    numToCalc = float(input('Please enter a positive integer')) # Enter an positive number which will be converted to a float
    Guess = numToCalc + 1 # This is done in order to initiate our 'guess' equation downstream as per Newton's method
    
    for i in range(numOfIterations): # Begin our 'for' loop
        Guess = (0.5) * (Guess + (numToCalc/Guess))  # Using Newtons method  ( x_(n+1) = 0.5 * (x_n +a / x_n)   )
    print('The square root of', numToCalc, 'is approx.' , round(Guess,1))  # Printing out the required output and rounding result to one decimal place
    return Guess   # Returning the value of Guess
    
sqrt()  # Calling the function. No arguement needs to be passed here due to the use of a default argument