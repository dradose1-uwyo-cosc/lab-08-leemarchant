# Lee Marchant
# UWYO COSC 1010
# 11/04/24
# Lab 8
# Lab Section: 14
# Sources, people worked with, help given to:


def check_value(value):
    """Checks if input value is an int or float"""
    if value.isdigit() or value[0] == '-' and value[1:].isdigit():
        return int(value)
    elif '.' in value:
        newvalue = value.replace('.', '', 1)
        if newvalue.isdigit() or value[0] == '-' and newvalue[1:].isdigit():
            return float(value)
        else: return False
    else:
        return False


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound

# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def slope_intercept(m, b, upper, lower):
    """Holds equation for point-slope"""
    y_list = []
    m = check_value(m)
    b = check_value(b)
    upper = check_value(upper)
    lower = check_value(lower)
    if m is not False and b is not False and upper is not False and lower is not False and (upper >= lower) and (type(upper) == int) and (type(lower) == int):
        for x in range(lower, upper + 1):
            y = m * x + b
            y_list.append(y)
        return y_list
    else:
        return False

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

while True:
    print(f'Enter "exit" to exit')
    input_m = input('Enter "m": ')
    if input_m.lower() == 'exit':
        break
    input_b = input('Enter "b": ')
    if input_b.lower() == 'exit':
        break
    input_upper = input('Enter upper bound: ')
    if input_upper.lower() == 'exit':
       break
    input_lower = input('Enter lower bound: ')
    if input_m.lower() == 'exit':
        break
    print(slope_intercept(input_m, input_b, input_upper, input_lower))
            

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


import math

def quad_form(a, b, c):
    """Holds equation for Quadratic Formula"""
    a = check_value(a)
    b = check_value(b)
    c = check_value(c)
    value = square_root(a,b,c)
    squrt = math.sqrt(value)
    if a is not False and b is not False and c is not False and square_root(a,b,c) is not False:
        squrt = math.sqrt(value)
        ans_1 = (-b + squrt)/ (2 * a)
        ans_2 = (-b - squrt)/ (2 * a)
        return (f'Answers: {ans_1}, {ans_2}')
    elif value is False:
        return (f'Null')
    else:
        return False
    
def square_root(a, b, c):
    """Holds equation within the square root"""
    value = (b**2 - (4*a*c))
    if value < 0:
        return False
    else:
        return value


while True:
    print(f'Enter "exit" to exit')
    user_a = input('Enter "a": ')
    if user_a == 'exit':
        break
    user_b = input('Enter "b": ')
    if user_b == 'exit':
        break
    user_c = input('Enter "c": ')
    if user_c == 'exit':
        break
    print(quad_form(user_a, user_b, user_c))