#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""
def hypotenuse(a,b):
    from math import sqrt
    print("Input lengths of shorter triangle sides:")
    a = float(input("a: "))
    b = float(input("b: "))

    c = sqrt(a**2 + b**2)
    print("The length of the hypotenuse is", c )

    #a = float(input("a"))
    
    #b = float(input("b"))
    
    #c = sqrt(a**2 + b**2)
     #       if c is True
      #      return c
    #else:
     #   c = False
