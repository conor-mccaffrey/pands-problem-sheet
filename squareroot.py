# ''Squareroot''
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Conor McCaffrey

def newton_method(number, number_iters = 5):
    
    a = float(number) # number to get square root of
    for i in range(number_iters): # iteration number
        number = 0.5 * (number + a / number) # update
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return number

print (newton_method(14.5))





