#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
numbera = int(input("Enter a number: "))
numberb = int(input("Enter another number: "))

number = [numbera, numberb]
max = max(number)
min = min(number)

import math
a = max%min

if a == 0:
    print(f"{min} is a factor of {max}")
else:
    print(f"{min} is not a factor of {max}")