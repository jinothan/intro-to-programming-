import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, θ):
   
   
    x = round (r * math.cos(math.radians(θ)), 5)
    y = round (r * math.sin(math.radians(θ)), 5)
    print(f"the coordinates = ({x}, {y})")
    return (x, y)

print ("Function 1")
r = float(input("what is the radius: "))
θ = float(input("what is the angle (in degrees): "))
polar_to_cartesian(r,θ)

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    r = round (math.sqrt(x**2 + y**2), 5)
    θ = round ((math.atan(y/x)), 5) #convert to radians
    print (f"the coordinates = ({r}, {θ})")
    return (r, θ)

print ("Function 2")
x =  float(input("what is the value of x: "))
y = float(input("what is the value of y: "))
cartesian_to_polar(x, y)

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    w = 2 * math.pi * f
    x_t= round(A * math.cos(w * t + math.radians(phi)),5) #equation
    print(f"The positon of the pendulum is {x_t}")
    return x_t

print ("Function 3")
A = float(input("what is the amplitude: "))
f = float(input("what is the value frequency: "))
phi= float(input("what is the value of phi (in degrees): "))
t = float(input("what is the value of time: "))
pendulum_position(A, f, phi, t)