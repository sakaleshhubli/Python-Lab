#area of triangle

import math
a = float(input("Enter the length of first slide: "))
b = float(input("Enter the length of second slide: "))
c = float(input("Enter the length of third slide: "))

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of triangle is", area)