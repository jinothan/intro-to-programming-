# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # variables
    g = 9.8 # acceleration due to gravity
    
    #Calculation
    h= h0 - 0.5*g*t**2
    print (f"Height of the ball at time {t} seconds = {h} meters")
    
#Input values:
h0 = float(input("Enter initial height (in meters):"))
t = float(input("Enter time (in seconds):"))
calculate_height(h0, t)

h0 = float(input("Enter initial height (in meters):"))
t = float(input("Enter time (in seconds):"))
calculate_height(h0, t)

h0 = float(input("Enter initial height (in meters):"))
t = float(input("Enter time (in seconds):"))
calculate_height(h0, t)



# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # variables
    speed = 20
    #Calculation
    distance = speed * t 
    #Output the result
    print (f"The car will travel {distance} meters in {t} second(s).")
t = float(input("Enter time (in seconds):"))
calculate_car_distance(t)

t = float(input("Enter time (in seconds):"))
calculate_car_distance(t)

t = float(input("Enter time (in seconds):"))
calculate_car_distance(t)


