"""
This program calculates and prints 
the gravitational force
between the Earth and the Sun  
using the grav_force variable.
"""

G = 6.67 * (10 ** -11) 
M_sun = 2.0 * (10 ** 30) 
M_earth = 6.0 * (10 ** 24) 
r = 1.5 * (10 ** 11) 


grav_force = (G * M_sun * M_earth) / r ** 2
print (grav_force)
