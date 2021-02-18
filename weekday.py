# Weekday Determination
# Program that outputs whether the current day is a weekday or not
# Author: Conor McCaffrey

import datetime  #import datetime module as per W3Schools 

weekDays = ['Monday','Tuesday','Wednesday','Thursday','Friday'] # List of all the weekdays
weekEnd = ['Saturday','Sunday'] # In this example, this list isn't needed but included for completeness

now = datetime.date.today() # Using datetime module, this code gets us the current date
today = ('{:%A}'.format(now)) # I am only interested in the string format of the current day. 
#The ':%A' was retreived from W3Schools and I've used 'format' attribute from previous tutorials

# Flow for searching through our weekDay list
if today in weekDays: # checking if our current day is in the weekDays list
    print('Yes, unfortunately today is a weekday') # Print this if current day is a weekday
elif today in weekEnd: # if current day is not a weekday, it must then be a Sat or Sun (a slight sanity check as this could easily be an 'else' clause)
    print('It is the weekend, yay!')  # code for if day is in the weekend