import math, cmath

c1 = 0.876+1.797j
c2 = -5.745-4.820j
pc = c1*c2
print(pc)
pc1 = cmath.polar(pc)
print(pc1)
print(math.degrees(pc1[1]))