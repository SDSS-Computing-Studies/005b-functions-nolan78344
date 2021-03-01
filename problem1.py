#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

import math
def hypotenuse(a,b,c):
    if c == True:
        (a**2 + b**2) = math.sqrt(c) 
        return c
    elif c == False:
        if a > b:
            (a**2 - b**2) = math.sqrt(c) 
            return c
        elif b > a:
            (b**2 - a**2) = math.sqrt(c) 
            return c