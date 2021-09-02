import cmath, math

# c1 = (3+4j)
# c2 = (2-3j)

# print(c1*c2)

# -12*j^2-j+6

c1 = (3+4j)/(2+3j)
c2 = (2j)/(2-3j)

mul = c1*c2

print(mul) # multiplication
polarcoordinates = cmath.polar(mul)
print("Polar Coordinates" , polarcoordinates) # polar coordinates (hypotenuse , angle in radian)
print(math.degrees(polarcoordinates[1])) # radians to degrees
