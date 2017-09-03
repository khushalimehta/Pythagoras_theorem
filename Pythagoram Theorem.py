from itertools import islice

import math

print("Pythagorean theorem calculator!")
print("Calculate your triangle sides.")
print("Asuume the sides are a, b,c and c is the hypotenuse(the side opposite to right angle)")
side = input("Which side(a,b,c) do you wish to calculate? Side:")
b = float(input("Input length of side 1:"))
c = float(input("Input length of side 2:"))
if side == 'a':
    ans = (c ** 2) - (b ** 2)
    ans = math.sqrt(ans)
    print("The length of side a is %g" %(ans))
elif side == 'b':
    ans = (c ** 2) - (a ** 2)
    ans = math.sqrt(ans)
    print("The length of side b is %g" %(ans))
elif side == 'c':
    ans = (a ** 2) + (b ** 2)
    ans = math.sqrt(ans)
    print("The length of side c is %g" %(ans))
else:
    print("Error!!")
