import math

# Focus
# X where bullet stop
# Variables:

#Bullet

# Simple Configuration
# Only Input aim, wind speed and direction
# The direction must be in degree, 0 to 360.



print("Welcome to the bullet simulator")
print("In the simple configuration, we use 9x19 Parabellum as the bullet")
print("With specifications as follow")
print("Mass = 7.45 grams")
print("Velocity = 360 metres/second")
print("Barrel length = 4.65 inches\n")

V0 = 360

aimX = -1
aimY = -1

while(aimX < 0 or aimX > 360):
    aimX = float(input("Shooting direction [Horizontal] (0 to 360 degrees): "))

# while(aimY < 0 or aimY > 360):
#     aimY = int(input("Shooting direction [Vertical] [0 degrees straight forward, 90 straight up] (0 to 360 degrees): "))

windDirection = float(input("Wind Direction (0 to 360 degrees): "))
windSpeed = float(input("Wind Speed [0 ... ]: "))
X = 0
Y = float(input("Height in which the bullet start[0 ... ]: "))

g = 9.8

# S = S0 + V0t + 1/2at^2
# S = V0t + 1/2at^2
# 0 = Y + V0t - 4,9 t ** 2
# if V = 0 => -Y = - 1/2gt**2
# == 2y/g = t**2
# == t = sqrt 2y/g
# if V != 0 => t   

t = math.sqrt(2*Y/g)

Xend = V0*t



print(t)
print("Bullet spot: ",Xend)
