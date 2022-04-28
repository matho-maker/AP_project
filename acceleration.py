import math as mt

#Acceleration functions for the given axis
def accel_x(m, g, mu, C, rho, area, v):
    a=(((mu*m*g)-(0.5*C*rho*area*(v**2)))/m)
    return(a)

def accel_y(m, rad, g, mu, C, rho, area, v):
    a=(((m*g*mt.sin(rad)-mu*m*g*mt.cos(rad))-(0.5*C*rho*area*(v**2)))/m)
    return(a)