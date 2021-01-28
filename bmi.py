# BMI Calculator
# Program to give the user their BMI based on their individual height and weight values
# Author: Conor McCaffrey

print('Hello, and welcome to your personal BMI calculator.')  # message to greet the user 
weight = float(input('Please enter your weight in kg, in numerical format :'))   # asking for weight in kg. Converting this value to a float for calculations 
height = float(input('Thank you, now please enter your height in cm, in numerical format :')) # asking for height in cm. Converting this value to a float for calculations 

convertToMetres = height / 100 # Converting our cm value to m^2 for BMI formula (retreived from Stack Overflow, referenced in README file)

BMI = ((weight / (convertToMetres**2)))  # now calculating the BMI based on given formula from question.

print ('Your BMI is {:.2f}'.format(BMI))  # Giving the user their BMI based on input values, rounding to two decimal places as per the example
print ('Thank you')   # Thanking the user for using the BMI program